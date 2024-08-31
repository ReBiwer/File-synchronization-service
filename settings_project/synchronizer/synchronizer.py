from settings_project.config.interaction_config import Config
from settings_project.working_directories.cloud_dir import CloudDir
from settings_project.working_directories.local_dir import LocalDir
from settings_project.types_project.type_info_file import InfoFile


class Synchronizer:
    def __init__(self, cloud: CloudDir, local: LocalDir):
        self.__cloud_dir = cloud
        self.__local_dir = local

    def check_updates_files(self):
        info_local_dir = self.__local_dir.get_info_dir()
        info_cloud_dir = self.__cloud_dir.get_info_dir()
        for info_file_local in info_local_dir:
            #  Проверка наличия файла в облаке. Если его нет, то загрузить
            if not (info_local_dir in info_cloud_dir):
                with open(info_file_local.path_file, 'rb') as downloadable_file:
                    self.__cloud_dir.load_file(info_file_local, downloadable_file)


if __name__ == '__main__':
    conf = Config()
    sync = Synchronizer(
        CloudDir(conf.token_API_cloud, conf.cloud_dir),
        LocalDir(conf.local_dir)
    )
    sync.check_updates_files()
