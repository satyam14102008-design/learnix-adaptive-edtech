from fastapi import APIRouter, Depends, Query
from typing import Optional
from app.api.deps import get_current_user
from app.database.connection import get_db
from app.services.multi_subject_curriculum import SUBJECTS
from app.services.grade_curriculum import GRADES

router = APIRouter(prefix="/api/student", tags=["Student"])

@router.get("/grades")
async def get_grades(user: dict = Depends(get_current_user)):
    db = get_db()
    student_id = user["_id"]
    learner_models_col = db.get_collection("learner_models")
    chapters_col = db.get_collection("chapters")
    concepts_col = db.get_collection("concepts")

    models = learner_models_col.find({"student_id": student_id})
    if not models:
        models = learner_models_col.find({"student_id": "student_alex_chen"})

    models_map = {m["concept_id"]: m for m in models}
    all_chapters = chapters_col.find({})
    all_concepts = concepts_col.find({})

    grade_list = []
    for g in GRADES:
        g_val = g["grade"]
        g_chapters = [ch for ch in all_chapters if ch.get("grade", 10) == g_val]
        g_ch_ids = {ch["id"] for ch in g_chapters}
        g_concepts = [c for c in all_concepts if c.get("grade", 10) == g_val or c.get("chapter_id") in g_ch_ids]
        g_models = [models_map[c["id"]] for c in g_concepts if c["id"] in models_map]

        if g_models:
            avg_m = round(sum(m.get("mastery_score", 0) for m in g_models) / len(g_models), 1)
            mastered_cnt = sum(1 for m in g_models if m.get("mastery_score", 0) >= 80)
        else:
            avg_m = g.get("average_mastery", 70.0)
            mastered_cnt = 3

        grade_list.append({
            **g,
            "average_mastery": avg_m,
            "total_chapters": len(g_chapters),
            "total_concepts": len(g_concepts),
            "mastered_concepts": mastered_cnt
        })

    return grade_list

@router.get("/subjects")
async def get_subjects(
    grade: Optional[int] = Query(None),
    user: dict = Depends(get_current_user)
):
    db = get_db()
    student_id = user["_id"]
    learner_models_col = db.get_collection("learner_models")
    chapters_col = db.get_collection("chapters")
    concepts_col = db.get_collection("concepts")

    models = learner_models_col.find({"student_id": student_id})
    if not models:
        models = learner_models_col.find({"student_id": "student_alex_chen"})

    models_map = {m["concept_id"]: m for m in models}
    all_chapters = chapters_col.find({})
    all_concepts = concepts_col.find({})

    if grade:
        all_chapters = [ch for ch in all_chapters if ch.get("grade", 10) == grade]

    subject_list = []
    for s in SUBJECTS:
        s_id = s["id"]
        s_chapters = [ch for ch in all_chapters if ch.get("subject_id", "physics") == s_id]
        s_chapter_ids = {ch["id"] for ch in s_chapters}
        s_concepts = [c for c in all_concepts if c.get("chapter_id") in s_chapter_ids or (c.get("subject_id") == s_id and (not grade or c.get("grade", 10) == grade))]
        
        s_models = [models_map[c["id"]] for c in s_concepts if c["id"] in models_map]
        
        if s_models:
            avg_m = round(sum(m.get("mastery_score", 0) for m in s_models) / len(s_models), 1)
            mastered_cnt = sum(1 for m in s_models if m.get("mastery_score", 0) >= 80)
        else:
            avg_m = 65.0
            mastered_cnt = 2

        subject_list.append({
            **s,
            "average_mastery": avg_m,
            "total_chapters": len(s_chapters),
            "total_concepts": len(s_concepts),
            "mastered_concepts": mastered_cnt
        })

    return subject_list

@router.get("/dashboard")
async def get_student_dashboard(
    subject: Optional[str] = Query(None),
    grade: Optional[int] = Query(None),
    user: dict = Depends(get_current_user)
):
    db = get_db()
    student_id = user["_id"]

    learner_models_col = db.get_collection("learner_models")
    chapters_col = db.get_collection("chapters")
    concepts_col = db.get_collection("concepts")
    attempts_col = db.get_collection("attempts")
    revision_col = db.get_collection("revision_schedules")

    # Fetch all concept models for this student
    models = learner_models_col.find({"student_id": student_id})
    if not models:
        models = learner_models_col.find({"student_id": "student_alex_chen"})

    all_chapters = chapters_col.find({}, sort=[("order", 1)])
    all_concepts = concepts_col.find({})
    models_map = {m["concept_id"]: m for m in models}
    concepts_map = {c["id"]: c for c in all_concepts}
    chapters_map = {ch["id"]: ch for ch in all_chapters}

    # Compute stats for all grades
    grade_list = []
    for g in GRADES:
        g_val = g["grade"]
        g_ch = [ch for ch in all_chapters if ch.get("grade", 10) == g_val]
        g_ch_ids = {ch["id"] for ch in g_ch}
        g_conc = [c for c in all_concepts if c.get("grade", 10) == g_val or c.get("chapter_id") in g_ch_ids]
        g_mods = [models_map[c["id"]] for c in g_conc if c["id"] in models_map]
        avg_m = round(sum(m.get("mastery_score", 0) for m in g_mods) / len(g_mods), 1) if g_mods else g.get("average_mastery", 70.0)
        mastered_cnt = sum(1 for m in g_mods if m.get("mastery_score", 0) >= 80) if g_mods else 3
        grade_list.append({
            **g,
            "average_mastery": avg_m,
            "total_chapters": len(g_ch),
            "total_concepts": len(g_conc),
            "mastered_concepts": mastered_cnt
        })

    # Filter by grade if selected
    active_grade = grade or 10
    filtered_chapters = [ch for ch in all_chapters if ch.get("grade", 10) == active_grade]
    if not filtered_chapters:
        filtered_chapters = all_chapters

    # Compute stats for each subject in this grade
    subject_stats = []
    for s in SUBJECTS:
        s_id = s["id"]
        s_ch = [ch for ch in filtered_chapters if ch.get("subject_id", "physics") == s_id]
        s_ch_ids = {ch["id"] for ch in s_ch}
        s_conc = [c for c in all_concepts if (c.get("chapter_id") in s_ch_ids or (c.get("subject_id") == s_id and c.get("grade", 10) == active_grade))]
        s_mods = [models_map[c["id"]] for c in s_conc if c["id"] in models_map]

        if s_mods:
            avg_m = round(sum(m.get("mastery_score", 0) for m in s_mods) / len(s_mods), 1)
            mastered_cnt = sum(1 for m in s_mods if m.get("mastery_score", 0) >= 80)
        else:
            avg_m = 65.0
            mastered_cnt = 2

        subject_stats.append({
            **s,
            "average_mastery": avg_m,
            "total_chapters": len(s_ch),
            "total_concepts": len(s_conc),
            "mastered_concepts": mastered_cnt
        })

    # Filter chapters and models if subject is selected
    if subject and subject != "all":
        chapters = [ch for ch in filtered_chapters if ch.get("subject_id", "physics") == subject]
    else:
        chapters = filtered_chapters

    active_ch_ids = {ch["id"] for ch in chapters}
    active_models = [m for m in models if m.get("chapter_id") in active_ch_ids]
    if not active_models:
        active_models = [m for m in models if m.get("grade", 10) == active_grade]

    # Compute overall mastery
    if active_models:
        overall_mastery = round(sum(m.get("mastery_score", 0) for m in active_models) / len(active_models), 1)
    else:
        overall_mastery = 68.0

    # Group by chapter
    chapter_stats = []
    for ch in chapters:
        ch_models = [m for m in models if m.get("chapter_id") == ch["id"]]
        if ch_models:
            avg_m = round(sum(m.get("mastery_score", 0) for m in ch_models) / len(ch_models), 1)
            mastered_cnt = sum(1 for m in ch_models if m.get("mastery_score", 0) >= 80)
        else:
            avg_m = 0.0
            mastered_cnt = 0
        chapter_stats.append({
            "chapter_id": ch["id"],
            "subject_id": ch.get("subject_id", "physics"),
            "subject_name": ch.get("subject_name", "Physics"),
            "title": ch["title"],
            "icon": ch.get("icon", "Book"),
            "color": ch.get("color", "from-blue-500 to-indigo-600"),
            "average_mastery": avg_m,
            "total_concepts": len(ch_models),
            "mastered_concepts": mastered_cnt
        })

    # Weak concepts (mastery < 55%)
    weak_concepts = [
        {
            "concept_id": m["concept_id"],
            "concept_name": m["concept_name"],
            "chapter_id": m.get("chapter_id", ""),
            "subject_id": chapters_map.get(m.get("chapter_id", ""), {}).get("subject_id", "physics"),
            "mastery_score": m.get("mastery_score", 0),
            "misconceptions_count": len(m.get("misconceptions_detected", [])),
            "current_difficulty": m.get("current_difficulty", "easy")
        }
        for m in sorted(active_models, key=lambda x: x.get("mastery_score", 0))
        if m.get("mastery_score", 0) < 55.0
    ][:6]

    # Strong concepts (> 75%)
    strong_concepts = [
        {
            "concept_id": m["concept_id"],
            "concept_name": m["concept_name"],
            "chapter_id": m.get("chapter_id", ""),
            "subject_id": chapters_map.get(m.get("chapter_id", ""), {}).get("subject_id", "physics"),
            "mastery_score": m.get("mastery_score", 0)
        }
        for m in sorted(active_models, key=lambda x: x.get("mastery_score", 0), reverse=True)
        if m.get("mastery_score", 0) >= 75.0
    ][:6]

    # Recommended next lesson
    weakest = weak_concepts[0] if weak_concepts else (models[0] if models else None)
    recommended_next = {
        "concept_id": weakest["concept_id"] if weakest else "c_resistance_factors",
        "concept_name": weakest["concept_name"] if weakest else "Resistance & Resistivity",
        "chapter_id": weakest.get("chapter_id", "electricity") if weakest else "electricity",
        "reason": "Active misconception detected requiring remediation",
        "estimated_minutes": 15
    }

    # Upcoming revision
    revisions = revision_col.find({"student_id": student_id}, limit=4)
    upcoming_revs = [
        {
            "concept_id": r.get("concept_id"),
            "concept_name": r.get("concept_name"),
            "chapter_id": r.get("chapter_id"),
            "due_date": r.get("due_date"),
            "status": r.get("status", "upcoming")
        }
        for r in revisions
    ]

    # Weekly activity data
    weekly_activity = [
        {"day": "Mon", "questions": 12, "accuracy": 78, "xp": 180},
        {"day": "Tue", "questions": 18, "accuracy": 82, "xp": 240},
        {"day": "Wed", "questions": 15, "accuracy": 71, "xp": 190},
        {"day": "Thu", "questions": 22, "accuracy": 89, "xp": 310},
        {"day": "Fri", "questions": 14, "accuracy": 79, "xp": 200},
        {"day": "Sat", "questions": 26, "accuracy": 85, "xp": 360},
        {"day": "Sun", "questions": 8, "accuracy": 88, "xp": 120}
    ]

    # Recent attempts
    recent_attempts = attempts_col.find({"student_id": student_id}, sort=[("timestamp", -1)], limit=5)

    # Badges
    achievements = [
        {"id": "b1", "title": "Ohm's Prodigy", "description": "Mastered Ohm's Law with 80%+ score", "icon": "Zap", "unlocked": True, "date": "2 days ago"},
        {"id": "b2", "title": "Streak Master", "description": "Completed a 5-day continuous learning streak", "icon": "Flame", "unlocked": True, "date": "Yesterday"},
        {"id": "b3", "title": "Optics Pioneer", "description": "Successfully completed Snell's law derivation", "icon": "Sun", "unlocked": True, "date": "3 days ago"},
        {"id": "b4", "title": "Misconception Buster", "description": "Corrected 3 fundamental physics fallacies", "icon": "ShieldCheck", "unlocked": False, "progress": "2/3"},
        {"id": "b5", "title": "Quantum Leap", "description": "Achieve 85% overall Class 10 Physics mastery", "icon": "Award", "unlocked": False, "progress": f"{overall_mastery}% / 85%"}
    ]

    greeting = f"Welcome back, {user.get('name', 'Learner')}!"

    return {
        "greeting": greeting,
        "student": {
            "id": user["_id"],
            "name": user.get("name", "Student"),
            "email": user.get("email"),
            "avatar": user.get("avatar"),
            "role": user.get("role"),
            "xp": user.get("xp", 1420),
            "level": user.get("level", 4),
            "level_title": user.get("level_title", "Quantum Apprentice"),
            "streak_days": user.get("streak_days", 6),
            "daily_goal": user.get("daily_goal", 5),
            "daily_completed": user.get("daily_completed", 3),
            "total_study_minutes": user.get("total_study_minutes", 240)
        },
        "stats": {
            "overall_mastery": overall_mastery,
            "total_concepts": len(models),
            "mastered_concepts": sum(1 for m in models if m.get("mastery_score", 0) >= 80),
            "learning_concepts": sum(1 for m in models if 50 <= m.get("mastery_score", 0) < 80),
            "weak_concepts_count": len(weak_concepts),
            "active_misconceptions": sum(len(m.get("misconceptions_detected", [])) for m in models)
        },
        "subjects": subject_stats,
        "subject_stats": subject_stats,
        "active_subject": subject or "all",
        "grades": grade_list,
        "active_grade": active_grade,
        "mastery_by_chapter": chapter_stats,
        "weak_concepts": weak_concepts,
        "strong_concepts": strong_concepts,
        "recommended_next_lesson": recommended_next,
        "upcoming_revisions": upcoming_revs,
        "weekly_activity": weekly_activity,
        "recent_attempts": recent_attempts,
        "achievements": achievements
    }

@router.get("/mastery")
async def get_student_mastery(user: dict = Depends(get_current_user)):
    db = get_db()
    learner_models_col = db.get_collection("learner_models")
    return learner_models_col.find({"student_id": user["_id"]})

@router.get("/learning-path")
async def get_learning_path(user: dict = Depends(get_current_user)):
    db = get_db()
    lp_col = db.get_collection("learning_paths")
    paths = lp_col.find({"student_id": user["_id"]})
    if not paths:
        # Fallback to general template
        paths = lp_col.find({"student_id": "student_alex_chen"})
    return paths

@router.get("/revisions")
async def get_revisions(user: dict = Depends(get_current_user)):
    db = get_db()
    rev_col = db.get_collection("revision_schedules")
    items = rev_col.find({"student_id": user["_id"]})
    if not items:
        items = rev_col.find({"student_id": "student_alex_chen"})
    return items
