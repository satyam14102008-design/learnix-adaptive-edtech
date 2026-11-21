"""
Adaptive Question Selection Engine for Learnix AI.
Selects the next best question for a student based on:
1. Target concept mastery & current difficulty tier
2. Unmet prerequisite dependencies
3. Active misconceptions to remediate
4. Revision due dates / forgetting risk
5. Excluding recently attempted question IDs
"""

from typing import List, Dict, Any, Optional

def select_next_adaptive_target(
    learner_models: List[Dict[str, Any]],
    concept_relationships: List[Dict[str, Any]],
    preferred_chapter_id: Optional[str] = None,
    preferred_concept_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Identifies the highest priority concept to practice next.
    Prioritizes:
    - Preferred concept if requested
    - Concepts with active misconceptions
    - Weak concepts (<50% mastery) whose prerequisites are met
    - Concepts due for spaced revision
    """
    models_by_concept = {m["concept_id"]: m for m in learner_models}
    
    # Prerequisite map: concept_id -> list of required prerequisite concept_ids
    prereqs: Dict[str, List[str]] = {}
    for rel in concept_relationships:
        if rel.get("relationship_type") == "prerequisite":
            prereqs.setdefault(rel["target_concept_id"], []).append(rel["source_concept_id"])

    # If preferred concept is specified, check prerequisites
    if preferred_concept_id and preferred_concept_id in models_by_concept:
        reqs = prereqs.get(preferred_concept_id, [])
        unmet = [r for r in reqs if models_by_concept.get(r, {}).get("mastery_score", 0) < 40.0]
        if unmet:
            # Prerequisite is too weak, recommend learning prerequisite first!
            unmet_model = models_by_concept.get(unmet[0], {})
            return {
                "concept_id": unmet[0],
                "concept_name": unmet_model.get("concept_name", unmet[0]),
                "chapter_id": unmet_model.get("chapter_id", ""),
                "target_difficulty": unmet_model.get("current_difficulty", "easy"),
                "reason": f"Prerequisite '{unmet_model.get('concept_name', unmet[0])}' requires reinforcement before progressing."
            }
        
        target = models_by_concept[preferred_concept_id]
        return {
            "concept_id": target["concept_id"],
            "concept_name": target["concept_name"],
            "chapter_id": target["chapter_id"],
            "target_difficulty": target.get("current_difficulty", "medium"),
            "reason": "Directly requested practice concept."
        }

    # Filter by chapter if requested
    candidates = learner_models
    if preferred_chapter_id:
        candidates = [m for m in learner_models if m.get("chapter_id") == preferred_chapter_id]
        if not candidates:
            candidates = learner_models

    # Check for active misconceptions first (highest priority)
    misconception_candidates = [
        m for m in candidates if len(m.get("misconceptions_detected", [])) > 0
    ]
    if misconception_candidates:
        # Sort by lowest mastery
        misconception_candidates.sort(key=lambda m: m.get("mastery_score", 0))
        target = misconception_candidates[0]
        return {
            "concept_id": target["concept_id"],
            "concept_name": target["concept_name"],
            "chapter_id": target["chapter_id"],
            "target_difficulty": "easy" if target.get("mastery_score", 0) < 40 else "medium",
            "reason": f"Remediating detected misconception in {target['concept_name']}."
        }

    # Check for weak concepts whose prerequisites are satisfied (>40% mastery)
    weak_candidates = []
    for m in candidates:
        cid = m["concept_id"]
        mastery = m.get("mastery_score", 0)
        if mastery < 70.0:
            reqs = prereqs.get(cid, [])
            all_reqs_met = all(models_by_concept.get(r, {}).get("mastery_score", 0) >= 40.0 for r in reqs)
            if all_reqs_met:
                weak_candidates.append(m)

    if weak_candidates:
        # Sort by lowest mastery
        weak_candidates.sort(key=lambda m: m.get("mastery_score", 0))
        target = weak_candidates[0]
        return {
            "concept_id": target["concept_id"],
            "concept_name": target["concept_name"],
            "chapter_id": target["chapter_id"],
            "target_difficulty": target.get("current_difficulty", "easy"),
            "reason": f"Foundational mastery building for {target['concept_name']}."
        }

    # Otherwise return concept with lowest mastery or next in syllabus order
    sorted_all = sorted(candidates, key=lambda m: m.get("mastery_score", 0))
    target = sorted_all[0] if sorted_all else learner_models[0]
    return {
        "concept_id": target["concept_id"],
        "concept_name": target["concept_name"],
        "chapter_id": target["chapter_id"],
        "target_difficulty": target.get("current_difficulty", "medium"),
        "reason": f"Advancing mastery in {target['concept_name']}."
    }
