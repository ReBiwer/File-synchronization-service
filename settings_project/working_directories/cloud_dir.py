import json
import requests
from datetime import datetime
from pprint import pprint
from settings_project.types_project.type_info_file import InfoFile
from settings_project.config.interaction_config import Config


class CloudDir:
    """Класс для взаимодействия с директорией в облаке"""
    __base_url_request = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, API_KEY: str, cloud_dir: str):
        self.__header = {'Authorization': API_KEY}
        self.__cloud_dir = cloud_dir

    def get_info_cloud_disk(self) -> tuple[dict, int]:
        """Метод возвращает информацию об диске"""
        response = requests.get(
            self.__base_url_request,
            headers=self.__header,
        )
        type_status_code = response.status_code
        type_info = json.loads(response.content)
        return type_info, type_status_code

    def __get_items_in_cloud_dir(self) -> list:
        """Метод возвращает список содержимого в облачной папке"""
        response = requests.get(
            self.__base_url_request + 'resources/?' + f'path={self.__cloud_dir}',
            headers=self.__header,
        )
        res = json.loads(response.content)['_embedded']['items']
        return res

    @staticmethod
    def __serializer_info_file(info_with_dict: dict) -> InfoFile:
        name_file = info_with_dict['name']
        created_time = datetime.strptime(info_with_dict['created'], "%Y-%m-%dT%H:%M:%S%z")
        modified_time = datetime.strptime(info_with_dict['modified'], "%Y-%m-%dT%H:%M:%S%z")
        return InfoFile(name_file=name_file, created_time=created_time, modified_time=modified_time)

    def get_info_dir(self) -> list[InfoFile]:
        info_about_files = list()
        for file in self.__get_items_in_cloud_dir():
            info_file = self.__serializer_info_file(file)
            info_about_files.append(info_file)
        return info_about_files


if __name__ == '__main__':
    conf = Config()
    key, cloud_dir = conf.token_API_cloud, conf.cloud_dir
    pprint(CloudDir(key, cloud_dir).get_info_dir())
