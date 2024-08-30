from settings_project.working_directories.cloud_dir import CloudDir
from settings_project.working_directories.local_dir import LocalDir


class Synchronizer:
    def __init__(self, cloud: CloudDir, local: LocalDir):
        self.__cloud_dir = cloud
        self.__local_dir = local

    def check_updates(self):
        pass
