import requests
from interaction_config import Config


class CloudDisk:
    """Класс для взаимодействия с облачным диском"""

    def __init__(self):
        self.__config = Config()
