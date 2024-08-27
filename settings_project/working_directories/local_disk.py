import os
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
        unix_time = os.path.getctime(path_file)
        return datetime.fromtimestamp(unix_time)

    @staticmethod
    def __get_time_modified(path_file: str) -> datetime:
        unix_time = os.path.getmtime(path_file)
        return datetime.fromtimestamp(unix_time)

    def __get_info_file(self, path_file: str) -> InfoFile:
        info = InfoFile(
            self.__get_time_created(path_file),
            self.__get_time_modified(path_file)
        )
        return info
