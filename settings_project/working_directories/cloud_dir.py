import requests
import json
from pprint import pprint
from settings_project.types_project.type_info_yandex_disk import ResponseMetaDataYandexDisk, ResponseStatus, User, SystemFolders
from settings_project.config.interaction_config import Config


class CloudDir:
    """Класс для взаимодействия с директорией в облаке"""
    __base_url_request = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self):
        self.__config = Config()
        self.__header = {'Authorization': self.__config.token_API_cloud}

    def get_info_cloud_disk(self) -> tuple[dict, int]:
        """Метод возвращает информацию об диске"""
        response = requests.get(
            self.__base_url_request,
            headers=self.__header,
        )
        type_status_code = response.status_code
        type_info = json.loads(response.content)
        return type_info, type_status_code

    def __get_items_in_cloud_dir(self) -> dict:
        """Метод возвращает список содержимого в облачной папке"""
        response = requests.get(
            self.__base_url_request + 'resources/?' + f'path={self.__config.cloud_dir}',
            headers=self.__header,
        )
        res = json.loads(response.content)['_embedded']['items']
        return res


if __name__ == '__main__':
    pprint(CloudDir().get_info_cloud_disk())
