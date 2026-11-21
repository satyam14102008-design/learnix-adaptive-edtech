import uuid
import datetime

def generate_id(prefix: str = "") -> str:
    """Generates a unique string ID with an optional prefix."""
    u = str(uuid.uuid4()).replace("-", "")[:12]
    return f"{prefix}_{u}" if prefix else u

def get_utc_now() -> str:
    """Returns the current ISO-formatted UTC timestamp string."""
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def parse_iso(dt_str: str) -> datetime.datetime:
    """Parses an ISO format string into datetime."""
    try:
        return datetime.datetime.fromisoformat(dt_str)
    except Exception:
        return datetime.datetime.now(datetime.timezone.utc)
