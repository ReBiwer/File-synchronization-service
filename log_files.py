import logging.config

import os

test_path = os.path.join(
    os.getcwd(), 'test_log_file'
)

dict_config = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "simple": {
                "format": f"%(levelname)s | %(asctime)s | %(lineno)s | %(funcName)s | %(message)s",
            },
        },
        "handlers": {
            "menu_handler": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "when": "h",
                "interval": 10,
                "backupCount": 5,
                "level": "DEBUG",
                "formatter": "menu_format",
                "filename": test_path,
                "encoding": "utf-8",
            },
        },
        "loggers": {
            'base_logger': {
                "level": "DEBUG",
                "handlers": ["base_handler", 'check_work', 'error_handler']
            },
        },
    }
