import os
from pprint import pprint
from settings_project.types_project.type_data_dir import InfoFile
from datetime import datetime
from settings_project.config.interaction_config import Config


class LocalDir:
    """Класс для взаимодействия с локальной директорией"""
    def __init__(self):
        self.__config = Config()
        self.__path_local_dir = self.__config.local_dir

    @staticmethod
    def __get_time_created(path_file: str) -> datetime:
        """
        Метод для получения времени создания файла
        :param path_file: путь к файлу (str)
        :return datetime: время создания файла (datetime)
        """
        unix_time = os.path.getctime(path_file)
        return datetime.fromtimestamp(unix_time)

    @staticmethod
    def __get_time_modified(path_file: str) -> datetime:
        """
        Метод для получения времени изменения файла
        :param path_file: путь к файлу (str)
        :return datetime: время изменения файла (datetime)
        """
        unix_time = os.path.getmtime(path_file)
        return datetime.fromtimestamp(unix_time)

    def __get_info_file(self, path_file: str) -> InfoFile:
        """
        Метод для информации о файле
        :param path_file: путь к файлу (str)
        :return InfoFile: информация о файле (InfoFile)
        """
        info = InfoFile(
            path_file,
            self.__get_time_created(path_file),
            self.__get_time_modified(path_file)
        )
        return info

    def get_info_dir(self) -> list[InfoFile]:
        """
        Метод для получения информации о файлах в локальной директории
        :return list[InfoFile]: список с информацией о каждом файле (за исключением директорий) в локальной директории
        """
        info_about_files = list()
        for file in os.listdir(self.__path_local_dir):
            path_file = os.path.join(self.__path_local_dir, file)
            if os.path.isfile(path_file):
                info_file = self.__get_info_file(path_file)
                info_about_files.append(info_file)
        return info_about_files


if __name__ == '__main__':
    for i in LocalDir().get_info_dir():
        print(i)
