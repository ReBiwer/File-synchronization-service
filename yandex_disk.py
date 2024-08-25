import requests
import json
from interaction_config import Config


class CloudDisk:
    """Класс для взаимодействия с облачным диском"""
    __base_url_request = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self):
        self.__config = Config()

    def get_meta_info_cloud_dir(self):
        response = requests.get(
            self.__base_url_request,
            headers={'Authorization': self.__config.token_API_cloud}
        )
        return json.loads(response.content)
