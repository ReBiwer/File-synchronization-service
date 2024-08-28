from settings_project.working_directories.Yandex_cloud_dir import YandexCloudDir
from settings_project.working_directories.local_disk import LocalDir


class Synchronizer:
    def __init__(self):
        self.__cloud_dir = YandexCloudDir()
        self.__local_dir = LocalDir()

    def check_updates(self):
        pass
