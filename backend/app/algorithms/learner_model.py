"""
Learner Model Mastery Algorithm for Learnix AI.
Implements deterministic, explainable, and continuous mastery updating.
Considers:
- Correctness
- Question difficulty (easy, medium, hard, advanced)
- Reasoning quality score (0.0 to 1.0)
- Repeated performance & historical streak
- Response time
- Previous mastery
- Confidence level
"""

from typing import Dict, Any, Tuple

DIFFICULTY_WEIGHTS = {
    "easy": 1.0,
    "medium": 1.4,
    "hard": 1.9,
    "advanced": 2.5
}

DIFFICULTY_THRESHOLDS = {
    "easy": (0, 35),
    "medium": (35, 65),
    "hard": (65, 85),
    "advanced": (85, 100)
}

def determine_recommended_difficulty(mastery: float) -> str:
    """Returns the question difficulty tier matched to the student's mastery level."""
    if mastery < 35.0:
        return "easy"
    elif mastery < 65.0:
        return "medium"
    elif mastery < 85.0:
        return "hard"
    else:
        return "advanced"

def calculate_mastery_delta(
    current_mastery: float,
    current_confidence: float,
    is_correct: bool,
    difficulty: str,
    reasoning_quality: float,
    response_time_seconds: float,
    has_misconception: bool = False,
    consecutive_correct: int = 0
) -> Tuple[float, float, Dict[str, Any]]:
    """
    Computes deterministic, explainable updates to mastery (0-100) and confidence (0-1).
    
    Returns:
        (new_mastery, new_confidence, breakdown_details)
    """
    diff_weight = DIFFICULTY_WEIGHTS.get(difficulty.lower(), 1.4)
    reasoning_score = max(0.0, min(1.0, reasoning_quality))
    
    # Time factor: expected response time range (10s to 120s)
    # Rushing (<6s) on a hard problem indicates guessing
    if response_time_seconds < 6.0 and difficulty in ["medium", "hard", "advanced"]:
        time_factor = 0.65
    elif 10.0 <= response_time_seconds <= 90.0:
        time_factor = 1.0
    elif response_time_seconds > 180.0:
        time_factor = 0.85  # struggling or delayed
    else:
        time_factor = 0.95

    breakdown = {}

    if is_correct:
        # Mastery headroom available
        headroom = max(1.0, 100.0 - current_mastery)
        
        # Base gain is scaled by remaining headroom so it never exceeds 100%
        # Foundational mastery increases faster; advanced mastery requires consistent precision
        base_rate = 0.22 if current_mastery < 50.0 else 0.16
        raw_gain = headroom * base_rate * (diff_weight / 1.4)
        
        # Reasoning multiplier:
        # High reasoning reinforces mastery; guess with 0 reasoning gives minimal reward
        reasoning_multiplier = 0.4 + (0.8 * reasoning_score)
        
        # Streak booster (up to 20% bonus for consecutive correct answers on this concept)
        streak_bonus = min(0.20, consecutive_correct * 0.05)
        
        delta = raw_gain * reasoning_multiplier * time_factor * (1.0 + streak_bonus)
        delta = max(2.0, min(22.0, delta))  # Bound single step delta
        
        new_mastery = min(100.0, current_mastery + delta)
        
        # Confidence increases
        conf_gain = 0.08 * reasoning_score * diff_weight
        new_confidence = min(1.0, current_confidence + conf_gain)
        
        explanation = f"Correct answer (+{delta:.1f}%). Reasoning quality: {int(reasoning_score*100)}% ({'verified conceptual mastery' if reasoning_score > 0.7 else 'partial reasoning'})."
        
    else:
        # If student fails, penalty is proportional to expected competency on this difficulty
        # Failing an 'easy' question when mastery is 70% shows severe conceptual gap
        current_tier = determine_recommended_difficulty(current_mastery)
        
        base_drop = 8.0
        if current_mastery > 70.0 and difficulty in ["easy", "medium"]:
            base_drop = 14.0  # High confidence student failing basic question
        elif current_mastery < 35.0 and difficulty in ["hard", "advanced"]:
            base_drop = 4.0   # Novice struggling on advanced problem is expected
            
        # Misconception penalty: explicit misconception requires targeted remediation
        misconception_factor = 1.35 if has_misconception else 1.0
        
        # If reasoning was completely off or stated a known misconception
        reasoning_penalty_factor = 1.2 if reasoning_score < 0.3 else 0.9
        
        delta = base_drop * misconception_factor * reasoning_penalty_factor
        delta = max(3.0, min(18.0, delta))
        
        new_mastery = max(5.0, current_mastery - delta)
        
        # Confidence drops
        conf_drop = 0.12 if has_misconception else 0.06
        new_confidence = max(0.1, current_confidence - conf_drop)
        
        explanation = f"Incorrect answer (-{delta:.1f}%). {'Misconception identified in reasoning.' if has_misconception else 'Review recommended before retrying.'}"

    new_difficulty = determine_recommended_difficulty(new_mastery)

    breakdown = {
        "previous_mastery": round(current_mastery, 1),
        "new_mastery": round(new_mastery, 1),
        "delta": round(new_mastery - current_mastery, 1),
        "previous_confidence": round(current_confidence, 2),
        "new_confidence": round(new_confidence, 2),
        "difficulty": difficulty,
        "recommended_next_difficulty": new_difficulty,
        "reasoning_score": round(reasoning_score, 2),
        "explanation": explanation
    }

    return round(new_mastery, 1), round(new_confidence, 2), breakdown
