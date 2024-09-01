from settings_project.config.interaction_config import Config
from settings_project.working_directories.cloud_dir import CloudDir
from settings_project.working_directories.local_dir import LocalDir
from settings_project.types_project.type_info_file import InfoFile
from settings_project.logging_project.log_files import log_func


class Synchronizer:
    def __init__(self, cloud: CloudDir, local: LocalDir):
        self.__cloud_dir = cloud
        self.__local_dir = local

    @staticmethod
    @log_func("Проверка наличия файла в директории")
    def __check_file_in_dir(file: InfoFile, files_in_dir: list[InfoFile]) -> bool:
        """
        Метод проверяет наличие файла в директории
        :param file: файл, который нежно проверить
        :param files_in_dir: директория, где нужно найти файл
        :return bool:
        """
        for file_dir in files_in_dir:
            if file_dir.name_file == file.name_file:
                return True
        return False

    @staticmethod
    @log_func("Проверка изменений файлов в директории")
    def __check_change_file(file: InfoFile, files_in_dir: list[InfoFile]) -> bool:
        """
        Метод проверят наличие изменений в файле относительно файла в директории
        :param file: проверяемый файл
        :param files_in_dir: директория, где идет поиск такого же файла
        :return bool:
        """
        for cloud_file in files_in_dir:
            if file.modified_time != cloud_file.modified_time:
                return True
        return False

    @log_func("Проверка удаленных файлов в директории")
    def __check_deleting_files_in_cloud(self, local_dir: list[InfoFile], cloud_dir: list[InfoFile]) -> None:
        """
        Метод проверяет удалялись ли файлы в локальной директории и удаляет их в облаке
        :param local_dir: локальная директория, где идет проверка удалений файлов
        :param cloud_dir: облачная директория, где происходит удаление файлов
        :return None:
        """
        for cloud_file in cloud_dir:
            if not self.__check_file_in_dir(cloud_file, local_dir):
                self.__cloud_dir.delete_file(cloud_file)

    @log_func("Проверка файлов в директории")
    def check_files(self) -> None:
        """
        Метод проверят все файлы в локальной директории
        :return:
        """
        local_dir = self.__local_dir.get_info_dir()
        cloud_dir = self.__cloud_dir.get_info_dir()
        for local_file in local_dir:
            if self.__check_file_in_dir(local_file, cloud_dir):
                if self.__check_change_file(local_file, cloud_dir):
                    with open(local_file.path_file, 'rb') as reloadable_file:
                        self.__cloud_dir.reload_file(local_file, reloadable_file)
            else:
                with open(local_file.path_file, 'rb') as downloadable_file:
                    self.__cloud_dir.load_file(local_file, downloadable_file)
        self.__check_deleting_files_in_cloud(local_dir, cloud_dir)


if __name__ == '__main__':
    conf = Config()
    sync = Synchronizer(
        CloudDir(conf.token_API_cloud, conf.cloud_dir),
        LocalDir(conf.local_dir)
    )
    sync.check_files()
