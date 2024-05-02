"""setup_logging.py: Setup logging configuration."""

import logging

from rich.logging import RichHandler

from config.constants import Constants


def setup_logging(
    logging_level: str = Constants.LOGGING_LEVEL_DEFAULT,
) -> logging.Logger:
    """
    Setup logging configuration.
    :param logging_level: The logging level to set.
    :return: The logger object.
    """
    valid_levels = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "NOTSET": logging.NOTSET,
    }

    if logging_level not in valid_levels:
        raise ValueError(
            f"Invalid logging level: {logging_level}. Valid levels are: {', '.join(valid_levels.keys())}"
        )

    logging.basicConfig(
        level=valid_levels[logging_level],
        format=Constants.LOGGING_FORMAT,
        datefmt=Constants.LOGGING_DATE_FORMAT,
        handlers=[RichHandler(rich_tracebacks=Constants.LOGGING_TRACEBACKS)],
    )

    return logging.getLogger("rich")
