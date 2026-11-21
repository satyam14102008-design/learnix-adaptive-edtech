from fastapi import APIRouter, Depends
from typing import List, Dict, Any
from app.api.deps import get_current_user
from app.database.connection import get_db
from app.schemas.models import TeacherDashboardResponse, CreateAssignmentRequest
from app.utils.helpers import generate_id, get_utc_now

router = APIRouter(prefix="/api/teacher", tags=["Teacher Analytics"])

@router.get("/dashboard", response_model=TeacherDashboardResponse)
async def get_teacher_dashboard(user: dict = Depends(get_current_user)):
    db = get_db()
    users_col = db.get_collection("users")
    learner_models_col = db.get_collection("learner_models")
    chapters_col = db.get_collection("chapters")
    concepts_col = db.get_collection("concepts")
    assignments_col = db.get_collection("assignments")

    students = users_col.find({"role": "student"})
    student_ids = [s["_id"] for s in students]

    all_models = learner_models_col.find({})
    chapters = chapters_col.find({}, sort=[("order", 1)])
    concepts = concepts_col.find({})

    # Compute student summaries
    student_summaries = []
    overall_mastery_sum = 0.0

    for s in students:
        s_models = [m for m in all_models if m.get("student_id") == s["_id"]]
        if s_models:
            avg_m = round(sum(m.get("mastery_score", 0) for m in s_models) / len(s_models), 1)
            weak_cnt = sum(1 for m in s_models if m.get("mastery_score", 0) < 50)
            total_q = sum(m.get("total_questions_answered", 0) for m in s_models)
        else:
            avg_m = 50.0
            weak_cnt = 3
            total_q = 12

        overall_mastery_sum += avg_m

        student_summaries.append({
            "id": s["_id"],
            "name": s.get("name", "Student"),
            "email": s.get("email"),
            "avatar": s.get("avatar"),
            "mastery": avg_m,
            "streak_days": s.get("streak_days", 1),
            "xp": s.get("xp", 100),
            "weak_concepts_count": weak_cnt,
            "total_questions_answered": total_q,
            "status": "At Risk" if avg_m < 50 else ("Excelling" if avg_m >= 75 else "On Track")
        })

    class_avg = round(overall_mastery_sum / max(1, len(students)), 1)
    at_risk_count = sum(1 for s in student_summaries if s["mastery"] < 50)
    active_streaks = sum(1 for s in student_summaries if s["streak_days"] >= 3)

    # Concept Gap Analysis (Class-wide average per concept)
    concept_stats = []
    for c in concepts:
        c_models = [m for m in all_models if m.get("concept_id") == c["id"]]
        if c_models:
            c_avg = round(sum(m.get("mastery_score", 0) for m in c_models) / len(c_models), 1)
            miscs_count = sum(len(m.get("misconceptions_detected", [])) for m in c_models)
        else:
            c_avg = 50.0
            miscs_count = 0
        concept_stats.append({
            "concept_id": c["id"],
            "concept_name": c["name"],
            "chapter_id": c.get("chapter_id"),
            "average_mastery": c_avg,
            "students_affected_by_misconception": miscs_count
        })

    weakest = sorted(concept_stats, key=lambda x: x["average_mastery"])[:5]
    strongest = sorted(concept_stats, key=lambda x: x["average_mastery"], reverse=True)[:5]

    # Misconception distribution
    misconception_map = {}
    for m in all_models:
        for misc_label in m.get("misconceptions_detected", []):
            misconception_map[misc_label] = misconception_map.get(misc_label, 0) + 1

    misconception_dist = [
        {"label": k, "students_count": v, "chapter": "Physics"}
        for k, v in sorted(misconception_map.items(), key=lambda x: x[1], reverse=True)[:6]
    ]

    # Chapter averages
    chapter_averages = []
    for ch in chapters:
        ch_concepts = [c["id"] for c in concepts if c.get("chapter_id") == ch["id"]]
        ch_models = [m for m in all_models if m.get("concept_id") in ch_concepts]
        if ch_models:
            ch_avg = round(sum(m.get("mastery_score", 0) for m in ch_models) / len(ch_models), 1)
        else:
            ch_avg = 50.0
        chapter_averages.append({
            "chapter_id": ch["id"],
            "title": ch["title"],
            "average_mastery": ch_avg
        })

    recent_assignments = assignments_col.find({"teacher_id": user.get("_id", "teacher_sarah_jenkins")}, limit=5)

    return {
        "total_students": len(students),
        "class_average_mastery": class_avg,
        "at_risk_students_count": at_risk_count,
        "active_streaks_count": active_streaks,
        "weakest_concepts": weakest,
        "strongest_concepts": strongest,
        "misconception_distribution": misconception_dist,
        "chapter_averages": chapter_averages,
        "students": student_summaries,
        "recent_assignments": recent_assignments
    }

@router.get("/concept-gaps")
async def get_concept_gaps():
    """Generates the Class Concept Heatmap: Rows = Concepts, Columns = Students."""
    db = get_db()
    users_col = db.get_collection("users")
    concepts_col = db.get_collection("concepts")
    learner_models_col = db.get_collection("learner_models")
    chapters_col = db.get_collection("chapters")

    students = users_col.find({"role": "student"})
    concepts = concepts_col.find({})
    models = learner_models_col.find({})
    chapters = chapters_col.find({})
    chapters_map = {ch["id"]: ch["title"] for ch in chapters}

    model_lookup = {(m.get("student_id"), m.get("concept_id")): m.get("mastery_score", 40.0) for m in models}

    matrix = []
    for c in concepts:
        row = {
            "concept_id": c["id"],
            "concept_name": c["name"],
            "chapter_name": chapters_map.get(c.get("chapter_id"), "General"),
            "student_scores": {}
        }
        for s in students:
            score = model_lookup.get((s["_id"], c["id"]), 45.0)
            row["student_scores"][s["_id"]] = {
                "student_name": s["name"],
                "score": score,
                "tier": "mastered" if score >= 80 else ("learning" if score >= 60 else ("needs_improvement" if score >= 40 else "weak"))
            }
        matrix.append(row)

    return {
        "students": [{"id": s["_id"], "name": s["name"], "avatar": s.get("avatar")} for s in students],
        "matrix": matrix
    }

@router.post("/assignments")
async def create_assignment(req: CreateAssignmentRequest, user: dict = Depends(get_current_user)):
    db = get_db()
    assignments_col = db.get_collection("assignments")
    users_col = db.get_collection("users")

    student_count = users_col.count_documents({"role": "student"})

    asg_doc = {
        "id": generate_id("asg"),
        "teacher_id": user["_id"],
        "title": req.title,
        "chapter_id": req.chapter_id,
        "target_concepts": req.target_concepts,
        "assigned_class": req.assigned_class,
        "due_date": req.due_date,
        "created_at": get_utc_now(),
        "total_assigned": student_count,
        "completed_count": 0,
        "average_score": 0.0
    }
    assignments_col.insert_one(asg_doc)
    return {"status": "success", "assignment": asg_doc}
