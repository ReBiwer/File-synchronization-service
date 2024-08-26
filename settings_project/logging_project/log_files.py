import logging.config
import os
from pathlib import Path


def _get_path_to_log() -> str:
    dir_project = os.path.join('PycharmProjects', 'File-synchronization-service')
    path_home = Path().cwd().home()
    path_log_file = os.path.abspath(
        os.path.join(
            path_home, dir_project, 'settings_project', 'logging_project', 'test_log_file'
        )
    )
    return path_log_file


def _get_dict_config() -> dict:
    dict_config = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "base_format": {
                "format": f"%(levelname)s | %(asctime)s | %(lineno)s | %(funcName)s | %(message)s",
            },
        },
        "handlers": {
            "base_handler": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "when": "h",
                "interval": 10,
                "backupCount": 5,
                "level": "DEBUG",
                "formatter": "base_format",
                "filename": _get_path_to_log(),
                "encoding": "utf-8",
            },
        },
        "loggers": {
            'base_logger': {
                "level": "DEBUG",
                "handlers": ["base_handler"]
            },
        },
    }
    return dict_config


def config_logger() -> None:
    logging.config.dictConfig(_get_dict_config())
