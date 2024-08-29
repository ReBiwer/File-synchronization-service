from typing import NamedTuple
from datetime import datetime


class InfoFile(NamedTuple):
    name_file: str
    path_file: str
    created_time: datetime
    modified_time: datetime

    def __str__(self):
        return (
            f'Имя файла: {self.name_file},'
            f'путь к файлу: {self.path_file}, '
            f'создан: {self.created_time}, '
            f'модифицирован: {self.modified_time}'
        )
