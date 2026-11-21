from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.models import SignupRequest, LoginRequest, AuthResponse
from app.database.connection import get_db
from app.utils.security import hash_password, verify_password, create_access_token
from app.utils.helpers import generate_id, get_utc_now
from app.api.deps import get_current_user

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/signup", response_model=AuthResponse)
async def signup(req: SignupRequest):
    db = get_db()
    users_col = db.get_collection("users")
    
    existing = users_col.find_one({"email": req.email.lower()})
    if existing:
        raise HTTPException(status_code=400, detail="Account with this email already exists")

    user_id = generate_id("usr")
    user_doc = {
        "_id": user_id,
        "email": req.email.lower(),
        "password_hash": hash_password(req.password),
        "name": req.name,
        "role": req.role,
        "grade": req.grade or "Class 10",
        "avatar": f"https://api.dicebear.com/7.x/bottts/svg?seed={req.name}",
        "xp": 100,
        "level": 1,
        "level_title": "Physics Initiate",
        "streak_days": 1,
        "daily_goal": 5,
        "daily_completed": 0,
        "total_study_minutes": 0,
        "created_at": get_utc_now()
    }
    users_col.insert_one(user_doc)

    # Initialize learner models for student
    if req.role == "student":
        concepts_col = db.get_collection("concepts")
        learner_models_col = db.get_collection("learner_models")
        concepts = concepts_col.find({})
        for c in concepts:
            learner_models_col.insert_one({
                "student_id": user_id,
                "concept_id": c["id"],
                "concept_name": c["name"],
                "chapter_id": c["chapter_id"],
                "mastery_score": 25.0,  # baseline initiate
                "confidence_level": 0.3,
                "total_questions_answered": 0,
                "correct_answers": 0,
                "incorrect_answers": 0,
                "last_studied": get_utc_now(),
                "current_difficulty": "easy",
                "misconceptions_detected": [],
                "revision_due_date": get_utc_now()
            })

    token = create_access_token({"sub": user_id, "role": req.role, "name": req.name})
    safe_user = {k: v for k, v in user_doc.items() if k != "password_hash"}
    return {"token": token, "user": safe_user}

@router.post("/login", response_model=AuthResponse)
async def login(req: LoginRequest):
    db = get_db()
    users_col = db.get_collection("users")

    user = users_col.find_one({"email": req.email.lower()})
    if not user or not verify_password(req.password, user.get("password_hash", "")):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": user["_id"], "role": user.get("role", "student"), "name": user.get("name")})
    safe_user = {k: v for k, v in user.items() if k != "password_hash"}
    return {"token": token, "user": safe_user}

@router.post("/demo-login/{role}", response_model=AuthResponse)
async def demo_login(role: str):
    """Provides instant 1-click access to pre-seeded demo accounts."""
    db = get_db()
    users_col = db.get_collection("users")

    target_id = "teacher_sarah_jenkins" if role.lower() == "teacher" else "student_alex_chen"
    user = users_col.find_one({"_id": target_id})
    if not user:
        raise HTTPException(status_code=404, detail="Demo account not found")

    token = create_access_token({"sub": user["_id"], "role": user.get("role", "student"), "name": user.get("name")})
    safe_user = {k: v for k, v in user.items() if k != "password_hash"}
    return {"token": token, "user": safe_user}

@router.get("/me")
async def get_me(user: dict = Depends(get_current_user)):
    safe_user = {k: v for k, v in user.items() if k != "password_hash"}
    return safe_user
