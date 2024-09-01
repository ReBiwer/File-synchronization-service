import configparser
import os
from settings_project.types_project.exceptions import (
    NoLocalPath,
    NoTokenAPI,
    NoCloudDir,
    NoTimeSynchronization,
    NoNameLogFile
)
from pathlib import Path


class Config:
    """
    Класс для работы с данными из config.ini
    Для работы с данными, необходимо создать экземпляр класса
    """

    def __init__(self):
        """При создании экземпляра класса, создает парсер и читает файл"""
        self.path_to_conf_file = self.__get_path_conf_file()
        self.__read_config_file()

    @staticmethod
    def __get_path_conf_file() -> str:
        """Метод возвращает абсолютный путь к файлу с конфигом, относительно директории PycharmProjects и проекта"""
        dir_project = os.path.join('PycharmProjects', 'File-synchronization-service')
        path_home = Path().cwd().home()
        path_config_file = os.path.abspath(
            os.path.join(
                path_home, dir_project, 'settings_project', 'config', 'config.ini'
            )
        )
        return path_config_file

    def __read_config_file(self) -> None:
        """Создает парсер и читает файл self.name_conf_file"""
        self.__config = configparser.ConfigParser()
        self.__config.read(self.path_to_conf_file)

    @property
    def token_API_cloud(self) -> str:
        """Возвращает токен доступа к облачному сервису"""
        try:
            return self.__config.get('API', 'token_API_cloud')
        except configparser.NoOptionError:
            raise NoTokenAPI('Не указана API токен облачного хранилища')

    @property
    def name_log_file(self) -> str:
        """Возвращает название лог файла"""
        try:
            return self.__config.get('logger', 'name_log_file')
        except configparser.NoOptionError:
            raise NoNameLogFile('Не указано имя для логфайла')

    @property
    def cloud_dir(self) -> str:
        """Возвращает название папки в облаке"""
        try:
            return self.__config.get('dirs', 'name_cloud_dir')
        except configparser.NoOptionError:
            raise NoCloudDir('Не указано имя директории в облаке')

    @property
    def local_dir(self) -> str:
        """Возвращает путь к локальной директории"""
        try:
            return self.__config.get('dirs', 'path_local_dir')
        except configparser.NoOptionError:
            raise NoLocalPath('Не указана локальная директория')

    @property
    def time_synchronization(self) -> int:
        """Возвращает периодичность синхронизации"""
        try:
            return int(self.__config.get('time_synchronization', 'time_sec'))
        except configparser.NoOptionError:
            raise NoTimeSynchronization('Не указан период синхронизации файлов')
