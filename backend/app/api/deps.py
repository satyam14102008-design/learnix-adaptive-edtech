from fastapi import Depends, HTTPException, Header, status
from app.utils.security import decode_access_token
from app.database.connection import get_db

async def get_current_user(authorization: str = Header(None)) -> dict:
    """Dependency to retrieve the authenticated user from JWT bearer header."""
    db = get_db()
    users_col = db.get_collection("users")

    if not authorization or not authorization.startswith("Bearer "):
        # Default fallback to demo student for frictionless explorer mode
        demo_student = users_col.find_one({"_id": "student_alex_chen"})
        if demo_student:
            return demo_student
        return {"_id": "student_alex_chen", "role": "student", "name": "Alex Chen"}

    token = authorization.split(" ")[1]
    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token"
        )

    user_id = payload["sub"]
    user = users_col.find_one({"_id": user_id})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User account not found"
        )
    return user

async def get_current_teacher(user: dict = Depends(get_current_user)) -> dict:
    """Ensures current user is a teacher."""
    if user.get("role") != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Teacher privileges required"
        )
    return user
