import json
import requests
from typing import BinaryIO
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

    def __serializer_info_file(self, info_with_dict: dict) -> InfoFile:
        name_file = info_with_dict['name']
        path_file = self.__cloud_dir + name_file
        created_time = datetime.strptime(info_with_dict['created'], "%Y-%m-%dT%H:%M:%S%z")
        modified_time = datetime.strptime(info_with_dict['modified'], "%Y-%m-%dT%H:%M:%S%z")
        return InfoFile(name_file, path_file, created_time, modified_time)

    def get_info_dir(self) -> list[InfoFile]:
        info_about_files = list()
        for info_file in self.__get_items_in_cloud_dir():
            info_file = self.__serializer_info_file(info_file)
            info_about_files.append(info_file)
        return info_about_files

    def __get_url_load(self, info_file: InfoFile) -> str:
        url = self.__base_url_request + f'resources/upload?path=/{self.__cloud_dir}/{info_file.name_file}'
        request = requests.get(
            url=url,
            headers=self.__header,
        )
        return request.json()['href']

    def load_file(self, info_file_cloud: InfoFile, downloadable_file: BinaryIO) -> int:
        url_upload_file = self.__get_url_load(info_file_cloud)
        response = requests.put(url_upload_file, headers=self.__header, data=downloadable_file)
        return response.status_code

    def delete_file(self, info_file_cloud: InfoFile) -> int:
        url = self.__base_url_request + f'resources?path=/{self.__cloud_dir}/{info_file_cloud.name_file}'
        response = requests.delete(url, headers=self.__header)
        return response.status_code

    def reload_file(self, info_file_cloud: InfoFile, reloadable_file: BinaryIO) -> tuple[int, int]:
        status_delete = self.delete_file(info_file_cloud)
        status_load = self.load(info_file_cloud, reloadable_file)
        return status_delete, status_load


if __name__ == '__main__':
    conf = Config()
    key, cloud_dir = conf.token_API_cloud, conf.cloud_dir
    file_cloud = InfoFile(
        name_file='Тестовый файл на ноуте.odt',
        path_file='/home/vladimir/test_local_dir/Тестовый файл на ноуте.odt',
        created_time=datetime.now(),
        modified_time=datetime.now()
    )
    cloud = CloudDir(key, cloud_dir)
    with open(file_cloud.path_file, 'rb') as file:
        pprint(cloud.reload_file(file_cloud, file))
