import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from app.database.connection import get_db
from app.services.seed_service import seed_database
from app.api import auth, student, learning, assessment, revision, teacher, ai

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[Learnix AI] Server starting up...")
    db = get_db()
    db.connect()
    seed_database(db)
    yield
    print("[Learnix AI] Server shutting down...")

app = FastAPI(
    title="Learnix AI Backend",
    description="Intelligent Adaptive Exam-Prep Learning Platform API",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(auth.router)
app.include_router(student.router)
app.include_router(learning.router)
app.include_router(assessment.router)
app.include_router(revision.router)
app.include_router(teacher.router)
app.include_router(ai.router)

@app.get("/")
async def root():
    return {
        "platform": "Learnix AI",
        "status": "operational",
        "version": "1.0.0",
        "syllabus": "Class 10 Physics",
        "docs": "/docs"
    }

@app.get("/api/health")
async def health_check():
    db = get_db()
    return {
        "status": "healthy",
        "database_connected": db.is_connected,
        "mode": "mongodb" if db.is_connected else "in_memory_high_perf"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
