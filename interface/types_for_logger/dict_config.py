from typing import TypedDict
from enum import Enum
import pprint

from interface.types_for_logger.settings_formatters import (
    FormatterLogger,
    SettingsBaseFormat,
    BaseFormat
)


class LevelLoggers(Enum):
    """Уровни логирования"""
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class TypeEncoding(str, Enum):
    """Значение кодировки для лог-файла"""
    encoding = 'UTF-8'


class DictConfigLogger(TypedDict):
    version: int
    disable_existing_loggers: bool
    formatters: FormatterLogger
    # handlers: HandlersLogger
    # loggers: NameLogger

def get_dict_config() -> DictConfigLogger:
    return DictConfigLogger(
        version=1,
        disable_existing_loggers=True,
        formatters=FormatterLogger(
            base_format=SettingsBaseFormat(
                format=BaseFormat.FORMAT.value
            )
        )
    )


test = get_dict_config()
# test['formatters']['base_format']
pprint.pprint(test)
