from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.

    Centralized runtime configuration for the backend.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "python-backend-automation-api"
    env: str = "local"  # local | staging | production
    log_level: str = "INFO"

    # Database configuration
    database_url: str = "sqlite:///./app.db"


settings = Settings()