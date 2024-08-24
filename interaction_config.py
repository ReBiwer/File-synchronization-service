import configparser


def _get_ConfigParser() -> configparser.ConfigParser:
    """Возращает парсер с прочитанным конфиг файлом"""
    config = configparser.ConfigParser()
    _read_config_file(config)
    return config


def _read_config_file(parser: configparser.ConfigParser) -> None:
    """Читает конфиг файл в переданном парсере"""
    parser.read('config.ini')


def get_keyOAuth() -> str:
    """Возвращает ключ доступа к диску"""
    config = _get_ConfigParser()
    return config.get("API", 'key_OAuth')


def get_name_log_file() -> str:
    """Возвращает имя лог файла"""
    config = _get_ConfigParser()
    return config.get('logger', 'name_log_file')


def get_name_cloud_dir() -> str:
    """Возвращает название папки в облаке"""
    config = _get_ConfigParser()
    return config.get('dirs', 'name_cloud_dir')


def get_path_local_dir() -> str:
    """Возвращает путь к локальной папке"""
    config = _get_ConfigParser()
    return config.get('dirs', 'path_local_dir')


def get_time_synchronization() -> int:
    """Возвращает период синхронизации (в секундах)"""
    config = _get_ConfigParser()
    return int(config.get('time_synchronization', 'time_sec'))
