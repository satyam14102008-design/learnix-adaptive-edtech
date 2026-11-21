"""
Database Connection & In-Memory MongoDB-compatible Document Store for Learnix AI.
Provides transparent fallbacks so the application runs immediately without requiring
a separate mongod service, while supporting native MongoDB when available.
"""

import os
import copy
import re
import asyncio
from typing import Dict, Any, List, Optional
import pymongo

class InMemoryCollection:
    """Implements core MongoDB collection methods in memory."""
    def __init__(self, name: str):
        self.name = name
        self.docs: List[Dict[str, Any]] = []

    def _matches(self, doc: Dict[str, Any], query: Dict[str, Any]) -> bool:
        if not query:
            return True
        for k, v in query.items():
            if k == "$or":
                if not any(self._matches(doc, q) for q in v):
                    return False
                continue
            if k == "$and":
                if not all(self._matches(doc, q) for q in v):
                    return False
                continue

            val = doc.get(k)
            if isinstance(v, dict):
                for op, op_val in v.items():
                    if op == "$eq" and val != op_val:
                        return False
                    elif op == "$ne" and val == op_val:
                        return False
                    elif op == "$gt" and not (val is not None and val > op_val):
                        return False
                    elif op == "$gte" and not (val is not None and val >= op_val):
                        return False
                    elif op == "$lt" and not (val is not None and val < op_val):
                        return False
                    elif op == "$lte" and not (val is not None and val <= op_val):
                        return False
                    elif op == "$in" and val not in op_val:
                        return False
                    elif op == "$nin" and val in op_val:
                        return False
            elif val != v:
                return False
        return True

    def find_one(self, query: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        query = query or {}
        for d in self.docs:
            if self._matches(d, query):
                return d.copy()
        return None

    def find(
        self,
        query: Optional[Dict[str, Any]] = None,
        sort: Optional[List[tuple]] = None,
        limit: int = 0,
        skip: int = 0
    ) -> List[Dict[str, Any]]:
        query = query or {}
        matched = [d.copy() for d in self.docs if self._matches(d, query)]
        if sort:
            for key, direction in reversed(sort):
                def sort_key(x):
                    val = x.get(key)
                    if val is None:
                        return (0, "")
                    if isinstance(val, (int, float)):
                        return (1, val)
                    return (2, str(val))
                matched.sort(key=sort_key, reverse=(direction < 0))
        if skip > 0:
            matched = matched[skip:]
        if limit > 0:
            matched = matched[:limit]
        return matched

    def insert_one(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        d = doc.copy()
        if "_id" not in d:
            import uuid
            d["_id"] = str(uuid.uuid4())
        self.docs.append(d)
        return {"inserted_id": d["_id"]}

    def insert_many(self, docs: List[Dict[str, Any]]) -> Dict[str, Any]:
        ids = []
        for doc in docs:
            res = self.insert_one(doc)
            ids.append(res["inserted_id"])
        return {"inserted_ids": ids}

    def update_one(self, query: Dict[str, Any], update: Dict[str, Any], upsert: bool = False) -> Dict[str, Any]:
        for i, d in enumerate(self.docs):
            if self._matches(d, query):
                self._apply_update(self.docs[i], update)
                return {"matched_count": 1, "modified_count": 1}
        if upsert:
            new_doc = copy.deepcopy(query)
            self._apply_update(new_doc, update)
            self.insert_one(new_doc)
            return {"matched_count": 0, "modified_count": 1, "upserted_id": new_doc.get("_id")}
        return {"matched_count": 0, "modified_count": 0}

    def update_many(self, query: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
        modified = 0
        for i, d in enumerate(self.docs):
            if self._matches(d, query):
                self._apply_update(self.docs[i], update)
                modified += 1
        return {"matched_count": modified, "modified_count": modified}

    def delete_one(self, query: Dict[str, Any]) -> Dict[str, Any]:
        for i, d in enumerate(self.docs):
            if self._matches(d, query):
                del self.docs[i]
                return {"deleted_count": 1}
        return {"deleted_count": 0}

    def delete_many(self, query: Dict[str, Any]) -> Dict[str, Any]:
        initial = len(self.docs)
        self.docs = [d for d in self.docs if not self._matches(d, query)]
        return {"deleted_count": initial - len(self.docs)}

    def count_documents(self, query: Optional[Dict[str, Any]] = None) -> int:
        query = query or {}
        return sum(1 for d in self.docs if self._matches(d, query))

    def _apply_update(self, doc: Dict[str, Any], update: Dict[str, Any]):
        for op, fields in update.items():
            if op == "$set":
                for k, v in fields.items():
                    doc[k] = copy.deepcopy(v)
            elif op == "$inc":
                for k, v in fields.items():
                    doc[k] = doc.get(k, 0) + v
            elif op == "$push":
                for k, v in fields.items():
                    if k not in doc or not isinstance(doc[k], list):
                        doc[k] = []
                    doc[k].append(copy.deepcopy(v))
            elif op == "$addToSet":
                for k, v in fields.items():
                    if k not in doc or not isinstance(doc[k], list):
                        doc[k] = []
                    if v not in doc[k]:
                        doc[k].append(copy.deepcopy(v))


class DatabaseManager:
    """Manages the MongoDB connection and collection routing."""
    def __init__(self):
        self.client = None
        self.db = None
        self.is_connected = False
        self.in_memory_collections: Dict[str, InMemoryCollection] = {}

    def connect(self):
        mongo_uri = os.getenv("MONGODB_URI")
        db_name = os.getenv("MONGODB_DB_NAME", "learnix")
        if not mongo_uri or os.getenv("USE_IN_MEMORY_DB", "false").lower() == "true":
            self.is_connected = False
            print("[Learnix DB] Initializing In-Memory High-Performance Document Store.")
            return

        try:
            client = pymongo.MongoClient(
                mongo_uri, 
                serverSelectionTimeoutMS=800,
                connectTimeoutMS=800,
                socketTimeoutMS=800
            )
            client.server_info()  # triggers connection attempt
            self.client = client
            self.db = client[db_name]
            self.is_connected = True
            print(f"[Learnix DB] Successfully connected to live MongoDB at {mongo_uri}")
        except Exception as e:
            self.is_connected = False
            try:
                if 'client' in locals() and client:
                    client.close()
            except Exception:
                pass
            print(f"[Learnix DB] Live MongoDB not reachable ({e}). Initializing In-Memory High-Performance Document Store.")

    def get_collection(self, name: str):
        if self.is_connected and self.db is not None:
            return self.db[name]
        if name not in self.in_memory_collections:
            self.in_memory_collections[name] = InMemoryCollection(name)
        return self.in_memory_collections[name]


db_manager = DatabaseManager()

def get_db():
    return db_manager
