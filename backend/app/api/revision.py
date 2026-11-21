from fastapi import APIRouter, Depends
from typing import Dict, Any
from pydantic import BaseModel
from app.api.deps import get_current_user
from app.database.connection import get_db
from app.algorithms.spaced_repetition import calculate_sm2_schedule
from app.utils.helpers import get_utc_now

router = APIRouter(prefix="/api/revision", tags=["Spaced Revision Center"])

class CompleteRevisionRequest(BaseModel):
    concept_id: str
    quality_score: int  # 0 to 5

@router.get("/due")
async def get_due_revisions(user: dict = Depends(get_current_user)):
    db = get_db()
    student_id = user["_id"]
    revision_col = db.get_collection("revision_schedules")
    learner_models_col = db.get_collection("learner_models")

    items = revision_col.find({"student_id": student_id})
    if not items:
        items = revision_col.find({"student_id": "student_alex_chen"})

    models = learner_models_col.find({"student_id": student_id})
    models_map = {m["concept_id"]: m for m in models}
    chapters_col = db.get_collection("chapters")
    ch_map = {ch["id"]: ch for ch in chapters_col.find({})}

    due_today = []
    overdue = []
    upcoming = []

    for item in items:
        cid = item.get("concept_id")
        m = models_map.get(cid, {})
        ch_info = ch_map.get(item.get("chapter_id"), {})
        entry = {
            "concept_id": cid,
            "concept_name": item.get("concept_name"),
            "chapter_id": item.get("chapter_id"),
            "grade": item.get("grade") or ch_info.get("grade", 10),
            "subject_id": ch_info.get("subject_id", "physics"),
            "subject_name": ch_info.get("subject_name", "Physics"),
            "due_date": item.get("due_date"),
            "mastery_score": m.get("mastery_score", 45.0),
            "interval_days": item.get("interval_days", 3),
            "repetition_count": item.get("repetition_count", 1),
            "status": item.get("status", "upcoming")
        }
        if item.get("status") == "overdue":
            overdue.append(entry)
        elif item.get("status") == "due_today":
            due_today.append(entry)
        else:
            upcoming.append(entry)

    return {
        "due_today": due_today,
        "overdue": overdue,
        "upcoming": upcoming,
        "total_due_count": len(due_today) + len(overdue),
        "streak_days": user.get("streak_days", 6),
        "estimated_session_minutes": (len(due_today) + len(overdue)) * 4
    }

@router.post("/complete")
async def complete_revision(req: CompleteRevisionRequest, user: dict = Depends(get_current_user)):
    db = get_db()
    student_id = user["_id"]
    revision_col = db.get_collection("revision_schedules")
    users_col = db.get_collection("users")

    item = revision_col.find_one({"student_id": student_id, "concept_id": req.concept_id})
    rep_count = item.get("repetition_count", 0) if item else 0
    ef = item.get("ease_factor", 2.5) if item else 2.5
    interval = item.get("interval_days", 1) if item else 1

    new_rep, new_ef, new_interval, due_date, meta = calculate_sm2_schedule(
        repetition_count=rep_count,
        ease_factor=ef,
        current_interval_days=interval,
        quality_score=req.quality_score
    )

    revision_col.update_one(
        {"student_id": student_id, "concept_id": req.concept_id},
        {
            "$set": {
                "due_date": due_date.isoformat(),
                "interval_days": new_interval,
                "ease_factor": new_ef,
                "repetition_count": new_rep,
                "last_reviewed": get_utc_now(),
                "status": "upcoming"
            }
        },
        upsert=True
    )

    users_col.update_one({"_id": student_id}, {"$inc": {"xp": 25}})

    return {
        "status": "success",
        "concept_id": req.concept_id,
        "new_interval_days": new_interval,
        "due_date": due_date.isoformat(),
        "ease_factor": new_ef,
        "message": f"Revision recorded! Next scheduled in {new_interval} day(s)."
    }
