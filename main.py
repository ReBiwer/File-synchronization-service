import time
from settings_project.synchronizer.synchronizer import Synchronizer
from settings_project.config.interaction_config import Config
from settings_project.working_directories.cloud_dir import CloudDir
from settings_project.working_directories.local_dir import LocalDir


if __name__ == '__main__':
    conf = Config()
    local_dir = LocalDir(conf.local_dir)
    cloud_dir = CloudDir(conf.token_API_cloud, conf.cloud_dir)
    sync = Synchronizer(cloud_dir, local_dir)
    while True:
        sync.check_files()
        time.sleep(conf.time_synchronization)
