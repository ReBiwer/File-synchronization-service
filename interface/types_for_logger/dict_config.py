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


class SettingsBaseFormat(TypedDict):
    """Настройки base_format"""
    format: str


class FormatterLogger(TypedDict):
    """Словарь с форматами в конфиге и их настройками
    Чтобы добавить новый формат, нужно прописать название формата (новый атрибут)
    и прописать настройки формата (создать новый класс с настройками)
    """
    base_format: SettingsBaseFormat


# class SettingsBaseHandler(TypedDict):
#     "class" = log
#
# class HandlersLogger(TypedDict):
#     """Словарь с командами логера и их настройками
#     Чтобы добавить новую команду, нужно прописать название команды (новый атрибут)
#     и прописать настройки команды (создать новый класс с настройками)"""
#     base_handler: SettingsBaseHandler

class DictConfigLogger(TypedDict):
    version: int
    disable_existing_loggers: bool
    formatters: FormatterLogger
    # handlers: HandlersLogger
    # loggers: NameLogger

test = DictConfigLogger(
    version=1,
    disable_existing_loggers=True,
    formatters=FormatterLogger(base_format=SettingsBaseFormat(format=f"%(levelname)s | %(asctime)s | %(lineno)s | %(funcName)s | %(message)s"))
)
# test['formatters']['base_format']
print(test['formatters']['base_format'])
