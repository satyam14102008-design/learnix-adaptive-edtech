"""
Gemini AI Client for Learnix AI.
Provides prompt synthesis and structured JSON generation using Gemini,
with automatic fallback to the deterministic local physics reasoning engine.
"""

import os
import json
import re
import asyncio
from typing import Dict, Any, Optional
from .prompt_templates import QUESTION_GENERATION_PROMPT, REASONING_ANALYSIS_PROMPT
from .fallback_engine import analyze_reasoning_fallback

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

def _clean_json_output(raw_text: str) -> Dict[str, Any]:
    """Extracts and parses JSON from markdown fenced code blocks or raw text."""
    text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1:
            return json.loads(text[start:end+1])
        raise

async def analyze_student_reasoning(
    question_text: str,
    concept_id: str,
    concept_name: str,
    student_answer: str,
    correct_answer: str,
    is_correct: bool,
    student_reasoning: str
) -> Dict[str, Any]:
    """Analyzes student reasoning using Gemini if available, or fallback engine."""
    if not GEMINI_API_KEY or len(GEMINI_API_KEY.strip()) < 10:
        return analyze_reasoning_fallback(
            question_text=question_text,
            concept_id=concept_id,
            student_answer=student_answer,
            correct_answer=correct_answer,
            is_correct=is_correct,
            reasoning_text=student_reasoning
        )

    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = REASONING_ANALYSIS_PROMPT.format(
            question_text=question_text,
            correct_answer=correct_answer,
            student_answer=student_answer,
            is_correct=str(is_correct),
            concept_name=concept_name,
            student_reasoning=student_reasoning
        )
        response = await asyncio.wait_for(model.generate_content_async(prompt), timeout=3.5)
        parsed = _clean_json_output(response.text)
        return parsed
    except Exception as e:
        print(f"[Learnix AI] Gemini reasoning analysis call failed or timed out ({e}), using fallback.")
        return analyze_reasoning_fallback(
            question_text=question_text,
            concept_id=concept_id,
            student_answer=student_answer,
            correct_answer=correct_answer,
            is_correct=is_correct,
            reasoning_text=student_reasoning
        )

async def generate_ai_question(
    chapter_id: str,
    chapter_name: str,
    concept_id: str,
    concept_name: str,
    difficulty: str,
    mastery: float,
    misconception: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Generates an adaptive question using Gemini API if available."""
    if not GEMINI_API_KEY or len(GEMINI_API_KEY.strip()) < 10:
        return None

    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = QUESTION_GENERATION_PROMPT.format(
            chapter_name=chapter_name,
            chapter_id=chapter_id,
            concept_name=concept_name,
            concept_id=concept_id,
            difficulty=difficulty,
            mastery=mastery,
            misconception=misconception or "None",
            recent_topics="standard syllabus coverage"
        )
        response = await asyncio.wait_for(model.generate_content_async(prompt), timeout=4.0)
        parsed = _clean_json_output(response.text)
        parsed["concept_id"] = concept_id
        parsed["chapter_id"] = chapter_id
        return parsed
    except Exception as e:
        print(f"[Learnix AI] Gemini question generation call failed or timed out ({e}).")
        return None
