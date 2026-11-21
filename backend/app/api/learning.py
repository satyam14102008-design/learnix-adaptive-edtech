from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional
from app.api.deps import get_current_user
from app.database.connection import get_db
from app.schemas.models import SubmitAnswerRequest, SubmitAnswerResponse, ConceptGraphResponse
from app.algorithms.adaptive_selection import select_next_adaptive_target
from app.algorithms.learner_model import calculate_mastery_delta
from app.algorithms.spaced_repetition import calculate_sm2_schedule
from app.ai.gemini_client import analyze_student_reasoning
from app.ai.misconception_database import find_misconception_by_id
from app.utils.helpers import generate_id, get_utc_now
from app.services.multi_subject_curriculum import SUBJECTS

router = APIRouter(prefix="/api/learning", tags=["Adaptive Learning"])

@router.get("/next-question")
async def get_next_question(
    grade: Optional[int] = Query(None),
    subject_id: Optional[str] = Query(None),
    chapter_id: Optional[str] = Query(None),
    concept_id: Optional[str] = Query(None),
    user: dict = Depends(get_current_user)
):
    db = get_db()
    student_id = user["_id"]

    learner_models_col = db.get_collection("learner_models")
    relationships_col = db.get_collection("concept_relationships")
    questions_col = db.get_collection("questions")
    concepts_col = db.get_collection("concepts")
    chapters_col = db.get_collection("chapters")

    models = learner_models_col.find({"student_id": student_id})
    if not models:
        # Fallback to demo models if new user hasn't initialized
        models = learner_models_col.find({"student_id": "student_alex_chen"})

    # If grade is specified, filter candidate models
    if grade and not chapter_id and not concept_id:
        grade_chapters = [ch for ch in chapters_col.find({}) if ch.get("grade", 10) == grade]
        if grade_chapters:
            grade_ch_ids = {ch["id"] for ch in grade_chapters}
            grade_models = [m for m in models if m.get("chapter_id") in grade_ch_ids or m.get("grade", 10) == grade]
            if grade_models:
                models = grade_models

    # If subject_id is specified without chapter, filter target search
    if subject_id and subject_id != "all" and not chapter_id:
        subj_chapters = chapters_col.find({"subject_id": subject_id})
        if subj_chapters:
            subj_ch_ids = {ch["id"] for ch in subj_chapters}
            subj_models = [m for m in models if m.get("chapter_id") in subj_ch_ids]
            if subj_models:
                models = subj_models

    rels = relationships_col.find({})

    # Run adaptive selection algorithm
    target = select_next_adaptive_target(
        learner_models=models,
        concept_relationships=rels,
        preferred_chapter_id=chapter_id,
        preferred_concept_id=concept_id
    )

    target_concept_id = target["concept_id"]
    target_difficulty = target["target_difficulty"]

    # Retrieve student's current mastery for this concept
    student_model = next((m for m in models if m["concept_id"] == target_concept_id), None)
    curr_mastery = student_model.get("mastery_score", 40.0) if student_model else 40.0

    # Find question matching concept & difficulty
    q_candidates = questions_col.find({"concept_id": target_concept_id})
    selected_q = None
    if q_candidates:
        # Prefer exact difficulty match
        diff_match = [q for q in q_candidates if q.get("difficulty") == target_difficulty]
        selected_q = diff_match[0] if diff_match else q_candidates[0]
    else:
        # If no question for specific concept, find another question from the same chapter or default
        chapter_candidates = questions_col.find({"chapter_id": target.get("chapter_id", "electricity")})
        if chapter_candidates:
            selected_q = chapter_candidates[0]
        elif grade:
            grade_qs = [q for q in questions_col.find({}) if q.get("grade", 10) == grade]
            selected_q = grade_qs[0] if grade_qs else questions_col.find_one({})
        elif subject_id and subject_id != "all":
            subj_qs = questions_col.find({"subject_id": subject_id})
            selected_q = subj_qs[0] if subj_qs else questions_col.find_one({})
        else:
            selected_q = questions_col.find_one({})

    if not selected_q:
        raise HTTPException(status_code=404, detail="No suitable questions available.")

    concept_doc = concepts_col.find_one({"id": selected_q.get("concept_id")}) or {}
    chapter_doc = chapters_col.find_one({"id": selected_q.get("chapter_id")}) or {}

    # Get prerequisites
    prereqs = [r["source_concept_id"] for r in rels if r.get("target_concept_id") == selected_q.get("concept_id")]

    return {
        "id": selected_q.get("id") or str(selected_q.get("_id")),
        "grade": selected_q.get("grade") or chapter_doc.get("grade", 10),
        "subject_id": selected_q.get("subject_id") or chapter_doc.get("subject_id", "physics"),
        "subject_name": selected_q.get("subject_name") or chapter_doc.get("subject_name", "Physics"),
        "chapter_id": selected_q.get("chapter_id"),
        "chapter_name": chapter_doc.get("title", "Topic"),
        "concept_id": selected_q.get("concept_id"),
        "concept_name": concept_doc.get("name", "Key Concept"),
        "difficulty": selected_q.get("difficulty", "medium"),
        "question_type": selected_q.get("question_type", "mcq"),
        "question_text": selected_q.get("question_text"),
        "options": selected_q.get("options", []),
        "hint": selected_q.get("hint"),
        "expected_reasoning": selected_q.get("expected_reasoning"),
        "prerequisites": prereqs,
        "current_mastery": curr_mastery,
        "selection_reason": target.get("reason", "Adaptive syllabus progression")
    }

@router.post("/submit-answer", response_model=SubmitAnswerResponse)
async def submit_answer(req: SubmitAnswerRequest, user: dict = Depends(get_current_user)):
    db = get_db()
    student_id = user["_id"]

    questions_col = db.get_collection("questions")
    learner_models_col = db.get_collection("learner_models")
    attempts_col = db.get_collection("attempts")
    users_col = db.get_collection("users")
    revision_col = db.get_collection("revision_schedules")

    # Find question
    q = questions_col.find_one({"id": req.question_id}) or questions_col.find_one({"_id": req.question_id})
    if not q:
        # Fallback question lookup
        q = questions_col.find_one({"concept_id": req.concept_id}) or questions_col.find_one({})

    correct_option = q.get("correct_answer", "A")
    is_correct = (req.selected_option.strip().upper() == correct_option.strip().upper())

    # Cognitive AI Reasoning & Misconception Analysis
    reasoning_eval = await analyze_student_reasoning(
        question_text=q.get("question_text", ""),
        concept_id=req.concept_id,
        concept_name=q.get("concept_id", "Physics Concept"),
        student_answer=req.selected_option,
        correct_answer=correct_option,
        is_correct=is_correct,
        student_reasoning=req.student_reasoning
    )

    reasoning_score = reasoning_eval.get("reasoning_score", 0.5)
    has_misconception = reasoning_eval.get("misconception_detected", False)
    misc_id = reasoning_eval.get("misconception_id")
    misconception_obj = find_misconception_by_id(misc_id) if misc_id else None

    # Fetch existing learner model
    lmodel = learner_models_col.find_one({"student_id": student_id, "concept_id": req.concept_id})
    if not lmodel:
        # Try demo model
        lmodel = learner_models_col.find_one({"student_id": "student_alex_chen", "concept_id": req.concept_id})
        if not lmodel:
            lmodel = {
                "student_id": student_id,
                "concept_id": req.concept_id,
                "mastery_score": 40.0,
                "confidence_level": 0.5,
                "current_difficulty": "medium",
                "total_questions_answered": 0,
                "correct_answers": 0,
                "incorrect_answers": 0,
                "misconceptions_detected": []
            }

    curr_mastery = float(lmodel.get("mastery_score", 40.0))
    curr_conf = float(lmodel.get("confidence_level", 0.5))

    # Calculate deterministic mastery update
    new_mastery, new_conf, breakdown = calculate_mastery_delta(
        current_mastery=curr_mastery,
        current_confidence=curr_conf,
        is_correct=is_correct,
        difficulty=q.get("difficulty", "medium"),
        reasoning_quality=reasoning_score,
        response_time_seconds=req.response_time_seconds,
        has_misconception=has_misconception,
        consecutive_correct=lmodel.get("correct_answers", 0)
    )

    # Update Learner Model in DB
    existing_miscs = list(lmodel.get("misconceptions_detected", []))
    if has_misconception and misconception_obj and misconception_obj["label"] not in existing_miscs:
        existing_miscs.append(misconception_obj["label"])
    elif is_correct and reasoning_score > 0.75 and existing_miscs:
        # Student overcame misconception with strong reasoning!
        existing_miscs.pop(0)

    learner_models_col.update_one(
        {"student_id": student_id, "concept_id": req.concept_id},
        {
            "$set": {
                "mastery_score": new_mastery,
                "confidence_level": new_conf,
                "current_difficulty": breakdown["recommended_next_difficulty"],
                "last_studied": get_utc_now(),
                "misconceptions_detected": existing_miscs
            },
            "$inc": {
                "total_questions_answered": 1,
                "correct_answers": 1 if is_correct else 0,
                "incorrect_answers": 0 if is_correct else 1
            }
        },
        upsert=True
    )

    # Update Spaced Repetition Schedule (SM-2)
    quality_score = 5 if (is_correct and reasoning_score > 0.8) else (
        4 if is_correct else (2 if not has_misconception else 1)
    )
    new_rep, new_ef, new_interval, due_date, sm2_meta = calculate_sm2_schedule(
        repetition_count=lmodel.get("repetition_count", 1),
        ease_factor=lmodel.get("ease_factor", 2.5),
        current_interval_days=lmodel.get("review_interval_days", 3),
        quality_score=quality_score
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
                "status": "upcoming" if new_interval > 1 else "due_today"
            }
        },
        upsert=True
    )

    # Award XP and update user streak
    xp_gain = 35 if is_correct else 10
    users_col.update_one(
        {"_id": student_id},
        {"$inc": {"xp": xp_gain, "daily_completed": 1}}
    )
    user_doc = users_col.find_one({"_id": student_id}) or {}
    streak = user_doc.get("streak_days", 6)

    # Log attempt
    attempt_doc = {
        "id": generate_id("att"),
        "student_id": student_id,
        "question_id": req.question_id,
        "concept_id": req.concept_id,
        "selected_option": req.selected_option,
        "is_correct": is_correct,
        "reasoning": req.student_reasoning,
        "reasoning_score": reasoning_score,
        "mastery_before": curr_mastery,
        "mastery_after": new_mastery,
        "misconception_detected": has_misconception,
        "response_time_seconds": req.response_time_seconds,
        "timestamp": get_utc_now()
    }
    attempts_col.insert_one(attempt_doc)

    return {
        "is_correct": is_correct,
        "correct_option": correct_option,
        "explanation": q.get("explanation", ""),
        "student_reasoning": req.student_reasoning,
        "reasoning_analysis": reasoning_eval,
        "misconception": misconception_obj,
        "remediation": misconception_obj["remediation"] if misconception_obj else (
            "Review the key formula and boundary conditions for this concept." if not is_correct else None
        ),
        "remediation_activity": misconception_obj.get("remediation_activity") if misconception_obj else None,
        "mastery_update": breakdown,
        "xp_awarded": xp_gain,
        "streak_days": streak,
        "next_question_ready": True
    }

@router.get("/concept-graph", response_model=ConceptGraphResponse)
async def get_concept_graph(
    grade: Optional[int] = Query(None),
    subject_id: Optional[str] = Query(None),
    user: dict = Depends(get_current_user)
):
    db = get_db()
    student_id = user["_id"]

    concepts_col = db.get_collection("concepts")
    relationships_col = db.get_collection("concept_relationships")
    learner_models_col = db.get_collection("learner_models")
    chapters_col = db.get_collection("chapters")

    all_concepts = concepts_col.find({})
    all_relationships = relationships_col.find({})
    all_chapters = chapters_col.find({}, sort=[("order", 1)])

    # Filter by grade if requested
    if grade:
        chapters = [ch for ch in all_chapters if ch.get("grade", 10) == grade]
        ch_ids = {ch["id"] for ch in chapters}
        concepts = [c for c in all_concepts if c.get("grade", 10) == grade or c.get("chapter_id") in ch_ids]
    else:
        chapters = all_chapters
        concepts = all_concepts

    # Filter by subject if requested
    if subject_id and subject_id != "all":
        chapters = [ch for ch in chapters if ch.get("subject_id", "physics") == subject_id]
        ch_ids = {ch["id"] for ch in chapters}
        concepts = [c for c in concepts if c.get("chapter_id") in ch_ids or c.get("subject_id") == subject_id]

    concept_ids = {c["id"] for c in concepts}
    relationships = [r for r in all_relationships if r.get("source_concept_id") in concept_ids and r.get("target_concept_id") in concept_ids]

    models = learner_models_col.find({"student_id": student_id})
    if not models:
        models = learner_models_col.find({"student_id": "student_alex_chen"})

    models_map = {m["concept_id"]: m for m in models}
    chapters_map = {ch["id"]: ch for ch in all_chapters}

    nodes = []
    for c in concepts:
        m = models_map.get(c["id"], {})
        mastery = float(m.get("mastery_score", 45.0))
        
        # Determine status & color tier
        if mastery >= 80.0:
            status = "mastered"
        elif mastery >= 60.0:
            status = "learning"
        elif mastery >= 40.0:
            status = "needs_improvement"
        else:
            status = "weak"

        ch = chapters_map.get(c.get("chapter_id"), {})
        
        nodes.append({
            "id": c["id"],
            "type": "conceptNode",
            "position": {"x": c.get("x", 100), "y": c.get("y", 100)},
            "data": {
                "id": c["id"],
                "grade": c.get("grade") or ch.get("grade", 10),
                "label": c["name"],
                "subject_id": c.get("subject_id") or ch.get("subject_id", "physics"),
                "subject_name": c.get("subject_name") or ch.get("subject_name", "Physics"),
                "chapter_id": c.get("chapter_id", ""),
                "chapter_name": ch.get("title", ""),
                "mastery": mastery,
                "confidence": float(m.get("confidence_level", 0.5)),
                "difficulty": m.get("current_difficulty", c.get("difficulty_baseline", "medium")),
                "status": status,
                "total_attempts": int(m.get("total_questions_answered", 0)),
                "correct_attempts": int(m.get("correct_answers", 0)),
                "misconceptions": m.get("misconceptions_detected", []),
                "formula": c.get("key_formula")
            }
        })

    edges = []
    for idx, r in enumerate(relationships):
        source_m = models_map.get(r["source_concept_id"], {}).get("mastery_score", 0)
        edges.append({
            "id": f"e_{r['source_concept_id']}_{r['target_concept_id']}_{idx}",
            "source": r["source_concept_id"],
            "target": r["target_concept_id"],
            "label": r.get("relationship_type", "prerequisite"),
            "animated": source_m < 50,
            "relationship_type": r.get("relationship_type", "prerequisite")
        })

    total_mastery = sum(n["data"]["mastery"] for n in nodes) / max(1, len(nodes))

    return {
        "nodes": nodes,
        "edges": edges,
        "chapters": chapters,
        "subjects": SUBJECTS,
        "overall_mastery": round(total_mastery, 1)
    }
