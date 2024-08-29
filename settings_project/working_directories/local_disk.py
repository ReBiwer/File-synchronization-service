import os
from settings_project.types_project.type_info_file import InfoFile
from datetime import datetime
from settings_project.config.interaction_config import Config


class LocalDir:
    """Класс для взаимодействия с локальной директорией"""
    def __init__(self, path_local_dir: str):
        self.__path_local_dir = path_local_dir

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

    def __serializer_info_file(self, path_file: str) -> InfoFile:
        """
        Метод для информации о файле
        :param path_file: путь к файлу (str)
        :return InfoFile: информация о файле (InfoFile)
        """
        name_file = os.path.basename(path_file)
        info = InfoFile(
            name_file,
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
    conf = Config()
    path_dir = conf.local_dir
    for i in LocalDir(path_dir).get_info_dir():
        print(i)
