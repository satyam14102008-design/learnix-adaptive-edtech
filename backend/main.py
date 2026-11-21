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

# Serve static frontend files if dist folder exists (Monolithic Deployments)
frontend_dist = os.path.join(os.path.dirname(__file__), "..", "frontend", "dist")
if os.path.exists(frontend_dist):
    from fastapi.staticfiles import StaticFiles
    from starlette.responses import FileResponse

    assets_dir = os.path.join(frontend_dist, "assets")
    if os.path.exists(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        if full_path.startswith("api") or full_path.startswith("docs") or full_path.startswith("openapi.json"):
            return {"detail": "Not Found"}
        file_path = os.path.join(frontend_dist, full_path)
        if full_path and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(frontend_dist, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
