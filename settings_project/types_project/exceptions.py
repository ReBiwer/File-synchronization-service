class NoLocalPath(Exception):
    """Ошибка возникает, когда не указана локальная директория"""
    pass


class NoTokenAPI(Exception):
    """Ошибка возникает, когда не указан токен облачного хранилища"""
    pass


class NoNameLogFile(Exception):
    """Ошибка возникает, когда не указано имя для лог файла"""
    pass


class NoCloudDir(Exception):
    """Ошибка возникает, когда не указано имя директории в облаке"""
    pass


class NoTimeSynchronization(Exception):
    """Ошибка возникает, когда не указано периодичность синхронизации"""
    pass
