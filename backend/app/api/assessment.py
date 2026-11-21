import asyncio
from fastapi import APIRouter, Depends
from typing import List, Dict, Any, Optional
from app.api.deps import get_current_user
from app.database.connection import get_db
from app.schemas.models import SubmitDiagnosticRequest
from app.ai.gemini_client import analyze_student_reasoning
from app.ai.misconception_database import find_misconception_by_id
from app.utils.helpers import get_utc_now

router = APIRouter(prefix="/api/assessment", tags=["Diagnostic Assessment"])

@router.post("/start")
async def start_diagnostic(
    grade: Optional[int] = None,
    subject_id: Optional[str] = None,
    user: dict = Depends(get_current_user)
):
    """Provides a balanced diagnostic covering subjects (Physics, Chemistry, Biology, Math) across grades."""
    db = get_db()
    questions_col = db.get_collection("questions")
    concepts_col = db.get_collection("concepts")
    chapters_col = db.get_collection("chapters")

    active_grade = grade or 10
    query = {"grade": active_grade}
    if subject_id and subject_id != "all":
        query["subject_id"] = subject_id
        title = f"Class {active_grade} {subject_id.capitalize()} Diagnostic Assessment"
    else:
        title = f"Class {active_grade} All-Subjects Comprehensive Diagnostic Assessment"

    chapters = chapters_col.find(query, sort=[("order", 1)])
    if not chapters:
        chapters = chapters_col.find({"grade": active_grade}, sort=[("order", 1)])
    if not chapters:
        chapters = chapters_col.find({}, sort=[("order", 1)])

    diagnostic_questions = []

    for ch in chapters:
        # Find representative question
        q = questions_col.find_one({"chapter_id": ch["id"]})
        if not q and grade:
            q = questions_col.find_one({"grade": active_grade})
        if q:
            concept = concepts_col.find_one({"id": q.get("concept_id")}) or {}
            diagnostic_questions.append({
                "id": q.get("id"),
                "grade": ch.get("grade", active_grade),
                "subject_id": ch.get("subject_id", "physics"),
                "subject_name": ch.get("subject_name", "Physics"),
                "chapter_id": ch["id"],
                "chapter_name": ch["title"],
                "concept_id": q.get("concept_id"),
                "concept_name": concept.get("name", "Key Concept"),
                "difficulty": q.get("difficulty", "medium"),
                "question_text": q.get("question_text"),
                "options": q.get("options", []),
                "hint": q.get("hint"),
                "requires_reasoning": True
            })

    # Limit to 8-10 questions if all subjects to prevent fatigue
    if not subject_id or subject_id == "all":
        diagnostic_questions = diagnostic_questions[:10]

    return {
        "assessment_id": f"diag_{subject_id or 'all'}_10th",
        "title": title,
        "total_questions": len(diagnostic_questions),
        "estimated_minutes": len(diagnostic_questions) * 2,
        "questions": diagnostic_questions
    }

@router.post("/submit")
async def submit_diagnostic(req: SubmitDiagnosticRequest, user: dict = Depends(get_current_user)):
    db = get_db()
    student_id = user["_id"]

    questions_col = db.get_collection("questions")
    learner_models_col = db.get_collection("learner_models")
    chapters_col = db.get_collection("chapters")
    lp_col = db.get_collection("learning_paths")

    results = []
    chapter_scores = {}
    misconceptions_found = []
    correct_count = 0

    # Pre-fetch questions and prepare async evaluation tasks in parallel
    eval_inputs = []
    for item in req.answers:
        q = questions_col.find_one({"id": item.question_id})
        if not q:
            continue
        is_corr = (item.selected_option.strip().upper() == q.get("correct_answer", "A").strip().upper())
        eval_inputs.append((item, q, is_corr))

    # Run reasoning analysis concurrently across all answers
    eval_tasks = [
        analyze_student_reasoning(
            question_text=q.get("question_text", ""),
            concept_id=item.concept_id,
            concept_name=q.get("concept_id", ""),
            student_answer=item.selected_option,
            correct_answer=q.get("correct_answer", "A"),
            is_correct=is_corr,
            student_reasoning=item.reasoning
        )
        for item, q, is_corr in eval_inputs
    ]
    evaluations = await asyncio.gather(*eval_tasks, return_exceptions=True)

    for (item, q, is_correct), reasoning_eval in zip(eval_inputs, evaluations):
        if is_correct:
            correct_count += 1

        if isinstance(reasoning_eval, Exception):
            reasoning_eval = {
                "reasoning_score": 0.5,
                "misconception_detected": False,
                "feedback_to_student": "Reasoning evaluated under fallback protocol."
            }

        has_misc = reasoning_eval.get("misconception_detected", False)
        misc_id = reasoning_eval.get("misconception_id")
        misc_obj = find_misconception_by_id(misc_id) if misc_id else None
        if misc_obj:
            misconceptions_found.append(misc_obj)

        # Baseline mastery estimation
        initial_m = 75.0 if is_correct and reasoning_eval.get("reasoning_score", 0) > 0.7 else (
            55.0 if is_correct else (35.0 if not has_misc else 25.0)
        )

        learner_models_col.update_one(
            {"student_id": student_id, "concept_id": item.concept_id},
            {
                "$set": {
                    "mastery_score": initial_m,
                    "confidence_level": 0.6 if is_correct else 0.35,
                    "current_difficulty": "medium" if initial_m >= 55 else "easy",
                    "misconceptions_detected": [misc_obj["label"]] if misc_obj else [],
                    "last_studied": get_utc_now()
                },
                "$inc": {
                    "total_questions_answered": 1,
                    "correct_answers": 1 if is_correct else 0,
                    "incorrect_answers": 0 if is_correct else 1
                }
            },
            upsert=True
        )

        ch_id = q.get("chapter_id", "general")
        chapter_scores.setdefault(ch_id, []).append(initial_m)

        results.append({
            "question_id": item.question_id,
            "concept_id": item.concept_id,
            "is_correct": is_correct,
            "correct_answer": q.get("correct_answer"),
            "explanation": q.get("explanation"),
            "reasoning_score": reasoning_eval.get("reasoning_score", 0.5),
            "feedback": reasoning_eval.get("feedback_to_student", "")
        })

    # Build chapter breakdown radar data
    chapters = chapters_col.find({}, sort=[("order", 1)])
    chapter_performance = []
    for ch in chapters:
        scores = chapter_scores.get(ch["id"], [50.0])
        avg = round(sum(scores) / len(scores), 1)
        chapter_performance.append({
            "chapter_id": ch["id"],
            "chapter_name": ch["title"],
            "score": avg
        })

    # Recommended Learning Path Generation
    weak_items = [r for r in results if not r["is_correct"]]
    new_path = []
    for idx, w in enumerate(weak_items):
        new_path.append({
            "student_id": student_id,
            "id": f"lp_diag_{idx+1}",
            "concept_id": w["concept_id"],
            "concept_name": w["concept_id"].replace("c_", "").replace("_", " ").title(),
            "priority": "Critical" if idx == 0 else "High",
            "estimated_minutes": 20,
            "status": "in_progress" if idx == 0 else "locked",
            "mastery_target": 75,
            "reason": "Identified in diagnostic onboarding test.",
            "recommended_activity": "Targeted conceptual review followed by 3 adaptive practice questions."
        })
    if new_path:
        lp_col.delete_many({"student_id": student_id})
        lp_col.insert_many(new_path)

    overall_accuracy = round((correct_count / max(1, len(req.answers))) * 100, 1)

    return {
        "status": "completed",
        "total_questions": len(req.answers),
        "correct_answers": correct_count,
        "overall_accuracy": overall_accuracy,
        "chapter_performance": chapter_performance,
        "misconceptions_detected": misconceptions_found,
        "question_breakdown": results,
        "learning_path_generated": len(new_path)
    }
