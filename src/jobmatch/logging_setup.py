"""Logging configuration for the ``jobmatch`` logger hierarchy."""

import logging
import sys

LOGGER_NAME = "jobmatch"
_HANDLER_NAME = "jobmatch-stderr"
_FORMAT = "%(asctime)s %(levelname)-8s %(name)s: %(message)s"


def configure_logging(level: str = "INFO") -> logging.Logger:
    """Attach a stderr handler to the package logger. Safe to call repeatedly."""
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(level)

    if not any(handler.get_name() == _HANDLER_NAME for handler in logger.handlers):
        handler = logging.StreamHandler(sys.stderr)
        handler.set_name(_HANDLER_NAME)
        handler.setFormatter(logging.Formatter(_FORMAT, datefmt="%H:%M:%S"))
        logger.addHandler(handler)

    return logger
