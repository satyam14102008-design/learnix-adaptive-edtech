from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.ai.gemini_client import generate_ai_question, analyze_student_reasoning
from app.ai.misconception_database import detect_misconception_in_text, find_misconception_by_id

router = APIRouter(prefix="/api/ai", tags=["AI Reasoning & Generation"])

class QuestionGenRequest(BaseModel):
    chapter_id: str
    chapter_name: str
    concept_id: str
    concept_name: str
    difficulty: str = "medium"
    mastery: float = 50.0
    misconception: Optional[str] = None

class ReasoningAnalysisRequest(BaseModel):
    question_text: str
    concept_id: str
    concept_name: str
    student_answer: str
    correct_answer: str
    is_correct: bool
    student_reasoning: str

class MisconceptionDetectRequest(BaseModel):
    reasoning_text: str
    concept_id: Optional[str] = None

@router.post("/generate-question")
async def api_generate_question(req: QuestionGenRequest):
    res = await generate_ai_question(
        chapter_id=req.chapter_id,
        chapter_name=req.chapter_name,
        concept_id=req.concept_id,
        concept_name=req.concept_name,
        difficulty=req.difficulty,
        mastery=req.mastery,
        misconception=req.misconception
    )
    if not res:
        # Return fallback mock structured response
        return {
            "question_text": f"Explain the principle governing {req.concept_name} under standard conditions.",
            "question_type": "mcq",
            "difficulty": req.difficulty,
            "options": [
                {"id": "A", "text": "Proportional direct relationship"},
                {"id": "B", "text": "Inverse reciprocal relationship"},
                {"id": "C", "text": "Constant independent parameter"},
                {"id": "D", "text": "Exponential degradation"}
            ],
            "correct_answer": "A",
            "explanation": f"In {req.chapter_name}, {req.concept_name} directly follows foundational physical laws.",
            "hint": "Check the governing formula for this concept."
        }
    return res

@router.post("/analyze-reasoning")
async def api_analyze_reasoning(req: ReasoningAnalysisRequest):
    return await analyze_student_reasoning(
        question_text=req.question_text,
        concept_id=req.concept_id,
        concept_name=req.concept_name,
        student_answer=req.student_answer,
        correct_answer=req.correct_answer,
        is_correct=req.is_correct,
        student_reasoning=req.student_reasoning
    )

@router.post("/detect-misconception")
async def api_detect_misconception(req: MisconceptionDetectRequest):
    res = detect_misconception_in_text(req.reasoning_text, req.concept_id or "")
    if res:
        return {"detected": True, "misconception": res}
    return {"detected": False, "misconception": None}
