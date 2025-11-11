"""
Configuration helpers for the Klomena backend.

We rely on `pydantic-settings` so that environment variables (or a local `.env`
file during development) can configure the application without editing code.
"""

from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application-wide configuration values."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: Literal["local", "test", "production"] = "local"
    database_url: str


@lru_cache
def get_settings() -> Settings:
    """Return a cached instance of the application settings."""

    return Settings()
