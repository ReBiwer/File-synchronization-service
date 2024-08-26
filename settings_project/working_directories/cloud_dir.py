import requests
import json

from settings_project.types_project.type_response import ResponseMetaDataYandexDisk, ResponseStatus, User, SystemFolders
from settings_project.config.interaction_config import Config


class CloudDir:
    """Класс для взаимодействия с облачным диском"""
    __base_url_request = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self):
        self.__config = Config()
        self.__header = {'Authorization': self.__config.token_API_cloud}

    @staticmethod
    def __typing_status_code_response(status_code: int) -> ResponseStatus:
        """Типизирует статус код ответа"""
        return ResponseStatus(status_code)

    @staticmethod
    def __typing_info_cloud_disk(info: dict) -> ResponseMetaDataYandexDisk:
        """Типизирует ответ от Яндекс-API на запрос информации о диске"""
        result = ResponseMetaDataYandexDisk(
            paid_max_file_size=info.get('paid_max_file_size', None),
            max_file_size=info.get('max_file_size', None),
            total_space=info.get('total_space', None),
            trash_size=info.get('trash_size', None),
            used_space=info.get('used_space', None),
            is_paid=info.get('is_paid', None),
            is_idm_managed_folder_address_access=info.get('is_idm_managed_folder_address_access', None),
            reg_time=info.get('reg_time', None),
            system_folders=SystemFolders(**info['system_folders']),
            user=User(**info['user']),
            is_idm_managed_public_access=info.get('is_idm_managed_public_access', None),
            payment_flow=info.get('payment_flow', None),
            unlimited_autoupload_enabled=info.get('unlimited_autoupload_enabled', None),
            revision=info.get('revision', None)
        )
        return result

    def get_info_cloud_disk(self) -> tuple[ResponseMetaDataYandexDisk, ResponseStatus]:
        """Метод возвращает информацию об диске"""
        response = requests.get(
            self.__base_url_request,
            headers=self.__header,
        )
        type_status_code = self.__typing_status_code_response(response.status_code)
        type_info = self.__typing_info_cloud_disk(json.loads(response.content))
        return type_info, type_status_code

    def get_info_cloud_dir(self) -> dict:
        """Метод возвращает информацию о папке в облаке"""
        response = requests.get(
            self.__base_url_request + 'resources/?' + f'path={self.__config.cloud_dir}',
            headers=self.__header,
        )
        return json.loads(response.content)
