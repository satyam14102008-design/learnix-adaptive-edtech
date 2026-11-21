"""
Fallback AI Engine for Learnix AI.
Provides deterministic, high-fidelity reasoning analysis and misconception detection
when the Gemini API key is not configured or during offline demo mode.
"""

from typing import Dict, Any, Optional
from .misconception_database import detect_misconception_in_text, find_misconception_by_id

# Concept keyword dictionaries to score scientific reasoning soundness
CONCEPT_KEYWORDS = {
    "electric_current": ["coulomb", "charge", "rate", "time", "ampere", "conserve", "flow"],
    "potential_difference": ["work", "charge", "energy", "joule", "volt", "pressure", "push"],
    "resistance_factors": ["length", "area", "resistivity", "rho", "collision", "proportional", "material"],
    "ohms_law": ["potential", "voltage", "current", "proportional", "constant", "temperature"],
    "series_circuits": ["same current", "sum", "divided", "additive", "single loop"],
    "parallel_circuits": ["same voltage", "branch", "reciprocal", "conductance", "pathway", "decreases"],
    "refraction_snell": ["speed", "wavelength", "optical density", "normal", "medium", "snell", "ratio"],
    "spherical_mirrors": ["focus", "pole", "center of curvature", "real", "virtual", "inverted", "diverge"],
    "lenses_refraction": ["focal length", "converge", "diverge", "convex", "concave", "refract"],
    "eye_defects": ["retina", "ciliary", "accommodation", "concave", "convex", "focal point", "elongated"],
    "light_scattering": ["wavelength", "rayleigh", "particles", "atmosphere", "blue", "red", "scatter"],
    "magnetic_fields": ["lines", "closed", "tangent", "never cross", "compass", "direction"],
    "solenoid_magnetic_field": ["uniform", "parallel", "inside", "turns", "core", "electromagnet"],
    "electrolytic_conduction": ["ions", "dissociate", "electrolyte", "cathode", "anode", "migration"],
    "newtons_first_law": ["inertia", "net force", "unbalanced", "constant velocity", "friction"],
    "newtons_second_law": ["momentum", "rate of change", "mass", "acceleration", "f=ma"],
    "newtons_third_law": ["action", "reaction", "different bodies", "equal and opposite", "pair"]
}

def analyze_reasoning_fallback(
    question_text: str,
    concept_id: str,
    student_answer: str,
    correct_answer: str,
    is_correct: bool,
    reasoning_text: str
) -> Dict[str, Any]:
    """Analyzes student reasoning deterministically."""
    trimmed = (reasoning_text or "").strip()
    
    if not trimmed:
        return {
            "reasoning_score": 0.4 if is_correct else 0.1,
            "is_sound": False,
            "misconception_detected": False,
            "misconception_label": None,
            "why_reasoning_flawed": "No reasoning provided. Showing an answer without explanation suggests guessing.",
            "feedback_to_student": "Make sure to explain your reasoning in full sentences so Learnix can verify your understanding!",
            "key_rule_to_remember": "Physics requires both accurate mathematical outcomes and conceptual justification."
        }

    # Step 1: Detect explicit misconceptions
    misc = detect_misconception_in_text(trimmed, concept_id)
    if misc:
        return {
            "reasoning_score": 0.2 if is_correct else 0.15,
            "is_sound": False,
            "misconception_detected": True,
            "misconception_id": misc["id"],
            "misconception_label": misc["label"],
            "why_reasoning_flawed": misc["why_incorrect"],
            "feedback_to_student": f"Noticeable misconception detected: '{misc['label']}'. {misc['remediation']}",
            "key_rule_to_remember": misc["why_incorrect"].split(".")[0] + "."
        }

    # Step 2: Score keyword relevance and logical depth
    lower = trimmed.lower()
    keywords = CONCEPT_KEYWORDS.get(concept_id, ["law", "formula", "proportional", "energy", "direction"])
    matched_keywords = [kw for kw in keywords if kw in lower]
    keyword_ratio = len(matched_keywords) / max(2, len(keywords) * 0.4)
    keyword_ratio = min(1.0, keyword_ratio)

    word_count = len(trimmed.split())
    length_score = min(1.0, word_count / 15.0)

    # Base score
    if is_correct:
        base_score = 0.5 + (0.35 * keyword_ratio) + (0.15 * length_score)
        base_score = min(0.98, max(0.55, base_score))
        return {
            "reasoning_score": round(base_score, 2),
            "is_sound": True,
            "misconception_detected": False,
            "misconception_label": None,
            "why_reasoning_flawed": None,
            "feedback_to_student": f"Excellent reasoning! You correctly identified key principles ({', '.join(matched_keywords[:3]) if matched_keywords else 'underlying physical laws'}).",
            "key_rule_to_remember": "Keep reinforcing the fundamental definitions and vector/sign conventions."
        }
    else:
        # Incorrect answer
        base_score = 0.2 + (0.25 * keyword_ratio)
        base_score = min(0.45, max(0.1, base_score))
        return {
            "reasoning_score": round(base_score, 2),
            "is_sound": False,
            "misconception_detected": False,
            "misconception_label": None,
            "why_reasoning_flawed": f"Your explanation mentioned {', '.join(matched_keywords[:2]) if matched_keywords else 'some terms'}, but arrived at an incorrect physical conclusion.",
            "feedback_to_student": "Carefully trace how each variable impacts the system before making your deduction.",
            "key_rule_to_remember": "Check equations and boundary conditions step-by-step."
        }
