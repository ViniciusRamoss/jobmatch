import logging
from collections.abc import Iterator

import pytest

from jobmath.logging_setup import LOGGER_NAME, configure_logging


@pytest.fixture(autouse=True)
def clean_logger() -> Iterator[None]:
    logger = logging.getLogger(LOGGER_NAME)
    yield
    logger.handlers.clear()
    logger.setLevel(logging.NOTSET)


def test_sets_level() -> None:
    logger = configure_logging("DEBUG")

    assert logger.level == logging.DEBUG


def test_is_idempotent() -> None:
    configure_logging()
    logger = configure_logging("WARNING")

    assert len(logger.handlers) == 1
    assert logger.level == logging.WARNING


def test_child_loggers_propagate(caplog: pytest.LogCaptureFixture) -> None:
    configure_logging("INFO")

    with caplog.at_level(logging.INFO, logger=LOGGER_NAME):
        logging.getLogger(f"{LOGGER_NAME}.sources").info("hello")

    assert "hello" in caplog.text
