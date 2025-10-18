"""Application configuration."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "Supply Management System"
    VERSION: str = "2.0.0"
    API_PREFIX: str = "/api/v1"

    # CORS settings
    BACKEND_CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"]

    # Database
    DATABASE_PATH: str = "../db/supply.db"

    class Config:
        case_sensitive = True


settings = Settings()
