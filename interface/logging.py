from typing import TypedDict, List
from enum import Enum
from logging import Handler


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


class FormatFormatterLogger(TypedDict):
    """Формат логгера"""
    format: str


class FormatterLogger(TypedDict):
    """Настройка формата логера"""
    name_format: FormatFormatterLogger


class SettingsHandlerLogger(TypedDict):
    """Настройки логера"""
    class_handler: Handler
    when: str | None
    interval: int | None
    backupCount: int | None
    level: LevelLoggers
    formatter: FormatterLogger
    filename: str
    encoding: TypeEncoding


class HandlerLogger(TypedDict):
    name_handler: SettingsHandlerLogger
