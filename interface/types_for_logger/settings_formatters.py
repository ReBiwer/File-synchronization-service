from typing import TypedDict
from enum import Enum


class BaseFormat(str, Enum):
    """Формат, который будет использоваться в BaseFormat"""
    FORMAT = f"%(levelname)s | %(asctime)s | %(lineno)s | %(funcName)s | %(message)s"


class SettingsBaseFormat(TypedDict):
    """Настройки base_format"""
    format: BaseFormat


class FormatterLogger(TypedDict):
    """Словарь с форматами в конфиге и их настройками
    Чтобы добавить новый формат, нужно прописать название формата (новый атрибут)
    и прописать настройки формата (создать новый класс с настройками)
    """
    base_format: SettingsBaseFormat
