from typing import NamedTuple
from datetime import datetime


class InfoFile(NamedTuple):
    created_time: datetime
    modified_time: datetime
