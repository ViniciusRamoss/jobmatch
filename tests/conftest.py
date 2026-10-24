from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Keep tests independent of the developer's real .env and environment."""
    monkeypatch.chdir(tmp_path)
    for name in ("JOBMATH_LOG_LEVEL", "JOBMATH_CONFIG_PATH"):
        monkeypatch.delenv(name, raising=False)
