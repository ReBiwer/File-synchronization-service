from settings_project.working_directories.cloud_dir import CloudDir
from settings_project.working_directories.local_disk import LocalDir


class Synchronizer:
    def __init__(self):
        self.__cloud_dir = CloudDir()
        self.__local_dir = LocalDir()

    def check_updates(self):
        pass
