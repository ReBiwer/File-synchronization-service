import configparser


class Config:
    """
    Класс для работы с данными из config.ini
    Для работы с данными, необходимо создать экземпляр класса
    """
    name_conf_file = 'config.ini'

    def __init__(self):
        """При создании экземпляра класса, создает парсер и читает файл"""
        self.__read_config_file()

    def __read_config_file(self) -> None:
        """Создает парсер и читает файл self.name_conf_file"""
        self.__config = configparser.ConfigParser()
        self.__config.read(self.name_conf_file)

    @property
    def token_API_cloud(self) -> str:
        """Возвращает токен доступа к облачному сервису"""
        return self.__config.get('API', 'token_API_cloud')

    @property
    def name_log_file(self) -> str:
        """Возвращает название лог файла"""
        return self.__config.get('logger', 'name_log_file')

    @property
    def cloud_dir(self) -> str:
        """Возвращает название папки в облаке"""
        return self.__config.get('dirs', 'name_cloud_dir')

    @property
    def local_dir(self) -> str:
        """Возвращает путь к локальной директории"""
        return self.__config.get('dirs', 'path_local_dir')

    @property
    def time_synchronization(self) -> int:
        """Возвращает периодичность синхронизации"""
        return int(self.__config.get('time_synchronization', 'time_sec'))
