import pytest
from typer.testing import CliRunner

from jobmath import __version__
from jobmath.cli import app

runner = CliRunner()


def test_version() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.output.strip() == __version__


def test_verbose_flag_is_accepted() -> None:
    result = runner.invoke(app, ["--verbose", "version"])

    assert result.exit_code == 0


def test_invalid_settings_exit_with_code_2(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("JOBMATH_LOG_LEVEL", "LOUD")

    result = runner.invoke(app, ["version"])

    assert result.exit_code == 2
    assert "Invalid environment settings" in result.output
