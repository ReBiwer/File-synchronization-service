import requests
import json

from types_project.type_response import ResponseMetaDataYandexDisk
from config.interaction_config import Config


class CloudDisk:
    """Класс для взаимодействия с облачным диском"""
    __base_url_request = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self):
        self.__config = Config()
        self.__header = {'Authorization': self.__config.token_API_cloud}

    def get_info_cloud_disk(self) -> ResponseMetaDataYandexDisk:
        """Метод возвращает информацию об диске"""
        response = requests.get(
            self.__base_url_request,
            headers=self.__header,
        )
        return json.loads(response.content)

    def get_info_cloud_dir(self) -> dict:
        """Метод возвращает информацию о папке в облаке"""
        response = requests.get(
            self.__base_url_request + 'resources/?' + f'path={self.__config.cloud_dir}',
            headers=self.__header,
        )
        return json.loads(response.content)
