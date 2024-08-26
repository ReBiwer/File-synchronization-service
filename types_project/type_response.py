from typing import TypedDict, Optional
from enum import Enum


class ResponseStatus(str, Enum):
    HTTP_200 = 200
    HTTP_400 = 400
    HTTP_401 = 401
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_406 = 406
    HTTP_413 = 413
    HTTP_423 = 423
    HTTP_429 = 429
    HTTP_503 = 503


class SystemFolders(TypedDict):
    odnoklassniki: Optional[str]  # Путь к папке "Социальные сети/Одноклассники"
    google: Optional[str]  # Путь к папке "Социальные сети/Google+"
    instagram: Optional[str]  # Путь к папке "Социальные сети/Instagram"
    vkontakte: Optional[str]  # Путь к папке "Социальные сети/ВКонтакте"
    attach: Optional[str]  # Путь к папке "Почтовые вложения"
    mailru: Optional[str]  # Путь к папке "Социальные сети/Мой Мир"
    downloads: Optional[str]  # Путь к папке "Загрузки"
    applications: Optional[str]  # Путь к папке "Приложения"
    facebook: Optional[str]  # Путь к папке "Социальные сети/Facebook"
    social: Optional[str]  # Путь к папке "Социальные сети"
    messenger: Optional[str]  # Путь к папке "Файлы Мессенджера"
    calendar: Optional[str]  # Путь к папке "Материалы встреч"
    photostream: Optional[str]  # Путь к папке "Фотокамера"
    screenshots: Optional[str]  # Путь к папке "Скриншоты"
    scans: Optional[str]  # Путь к папке "Сканы"


class User(TypedDict):
    reg_time: Optional[str]  # Дата регистрации Диска
    display_name: Optional[str]  # Отображаемое имя
    uid: Optional[str]  # Идентификатор пользователя
    country: Optional[str]  # Страна
    is_child: Optional[bool]  # Признак того что аккаунт является детским
    login: Optional[str]  # Логин


class ResponseMetaDataYandexDisk(TypedDict):
    paid_max_file_size: Optional[int]  # Общий объем диска
    max_file_size: Optional[int]  # Максимальный поддерживаемый размер файла
    total_space: Optional[int]  # Общий объем диска (байт)
    trash_size: Optional[int]  # Общий размер файлов в Корзине (байт). Входит в used_space
    used_space: Optional[int]  # Используемый объем диска
    is_paid: Optional[bool]  # Признак наличия купленного места
    is_idm_managed_folder_address_access: Optional[bool]  # Признак управления адресным доступом
    # публичным доступом для папок
    reg_time: Optional[str]  # Дате регистрации Диска
    system_folders: Optional[SystemFolders]
    user: Optional[User]
    is_idm_managed_public_access: Optional[bool]  # Признак управления адресным доступом публичным доступом для файлов
    payment_flow: Optional[bool]  # Признак причастности пользователя для payment_flow
    unlimited_autoupload_enabled: Optional[bool]  # Признак включенной безлимитной автозагрузки с мобильных устройств
    revision: Optional[int]  # Текущая ревизия Диска
