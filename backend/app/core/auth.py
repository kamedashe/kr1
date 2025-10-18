"""Basic authentication for the application."""
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

# Simple hardcoded users for basic auth (без bcrypt для спрощення)
USERS_DB = {
    "admin": {
        "username": "admin",
        "password": "admin",  # В продакшені використовуйте хешовані паролі!
        "full_name": "Administrator",
        "role": "admin"
    },
    "user": {
        "username": "user",
        "password": "user",  # В продакшені використовуйте хешовані паролі!
        "full_name": "Regular User",
        "role": "user"
    }
}


def authenticate_user(username: str, password: str) -> Optional[dict]:
    """Authenticate a user."""
    user = USERS_DB.get(username)
    if not user:
        return None
    # Проста перевірка пароля (в продакшені використовуйте хешування!)
    if password != user["password"]:
        return None
    return user


def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> dict:
    """Get current authenticated user."""
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


# Optional dependency - can be used to protect routes
def get_current_active_user(current_user: dict = Depends(get_current_user)) -> dict:
    """Get current active user."""
    return current_user
