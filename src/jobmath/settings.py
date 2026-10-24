"""Runtime settings read from environment variables and an optional .env file.

Secrets and machine-specific values live here; the candidate profile and
ranking preferences live in the YAML config (see ``config.py``).
"""

from pathlib import Path
from typing import Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="JOBMATH_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    log_level: LogLevel = "INFO"
    config_path: Path = Path("config/config.yaml")

    @field_validator("log_level", mode="before")
    @classmethod
    def _uppercase_level(cls, value: object) -> object:
        return value.upper() if isinstance(value, str) else value


def get_settings() -> Settings:
    return Settings()
