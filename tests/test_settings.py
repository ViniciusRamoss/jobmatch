from pathlib import Path

import pytest
from pydantic import ValidationError

from jobmatch.settings import Settings


def test_defaults() -> None:
    settings = Settings()

    assert settings.log_level == "INFO"
    assert settings.config_path == Path("config/config.yaml")


def test_reads_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("JOBMATCH_LOG_LEVEL", "debug")
    monkeypatch.setenv("JOBMATCH_CONFIG_PATH", "other.yaml")

    settings = Settings()

    assert settings.log_level == "DEBUG"
    assert settings.config_path == Path("other.yaml")


def test_reads_dotenv_file(tmp_path: Path) -> None:
    (tmp_path / ".env").write_text("JOBMATCH_LOG_LEVEL=WARNING\n", encoding="utf-8")

    assert Settings().log_level == "WARNING"


def test_rejects_invalid_level(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("JOBMATCH_LOG_LEVEL", "LOUD")

    with pytest.raises(ValidationError):
        Settings()
