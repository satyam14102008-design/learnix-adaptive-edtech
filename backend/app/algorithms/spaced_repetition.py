"""
SuperMemo-2 (SM-2) Spaced Repetition Algorithm for Learnix AI.
Computes optimal revision intervals and ease factors for concept retention.
"""

import datetime
from typing import Dict, Any, Tuple

DEFAULT_EASE_FACTOR = 2.5
MIN_EASE_FACTOR = 1.3

def calculate_sm2_schedule(
    repetition_count: int,
    ease_factor: float,
    current_interval_days: int,
    quality_score: int  # 0 to 5
) -> Tuple[int, float, int, datetime.datetime, Dict[str, Any]]:
    """
    Computes the next revision interval and updated ease factor based on SM-2.
    
    Quality Score scale:
    5 - Perfect response with sound scientific reasoning
    4 - Correct answer after slight hesitation or minor reasoning omission
    3 - Correct answer but weak reasoning / likely guessed
    2 - Incorrect answer, but remembered key formula/rule once prompted
    1 - Incorrect answer with active misconception detected
    0 - Complete unfamiliarity / blackout
    
    Returns:
        (new_repetitions, new_ease_factor, new_interval_days, due_date, metadata)
    """
    q = max(0, min(5, quality_score))
    ef = max(MIN_EASE_FACTOR, ease_factor)

    if q >= 3:
        # Successful recall
        if repetition_count == 0:
            new_interval = 1
        elif repetition_count == 1:
            new_interval = 3
        else:
            new_interval = int(round(current_interval_days * ef))
            # Bound realistic intervals
            new_interval = max(new_interval, current_interval_days + 1)
        
        new_repetitions = repetition_count + 1
    else:
        # Failed recall - reset repetition streak
        new_repetitions = 0
        new_interval = 1

    # Update Ease Factor: EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))
    delta_ef = 0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)
    new_ef = max(MIN_EASE_FACTOR, ef + delta_ef)
    new_ef = round(new_ef, 2)

    now = datetime.datetime.now(datetime.timezone.utc)
    due_date = now + datetime.timedelta(days=new_interval)

    metadata = {
        "quality_score": q,
        "previous_interval_days": current_interval_days,
        "new_interval_days": new_interval,
        "previous_ease_factor": ef,
        "new_ease_factor": new_ef,
        "repetition_count": new_repetitions,
        "due_date_iso": due_date.isoformat(),
        "is_mastered_retention": new_interval >= 14
    }

    return new_repetitions, new_ef, new_interval, due_date, metadata
