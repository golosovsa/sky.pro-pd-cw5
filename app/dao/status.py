"""
    DAO abstraction level
    Status DAO
"""

from typing import Optional, List, Type

from .base import BaseDAO
from .models import Status


class StatusDAO(BaseDAO[Status]):
    __model__: Type[Status] = Status
    _data: Status = Status(id=0, user_pk=0, current_page="start")

    def get_by_id(self, pk: int) -> Optional[Status]:
        return self._data

    def get_all(self) -> List[Status]:
        return [self._data, ]

    def create(self, model: Status):
        pass

    def update(self, model: Status):
        self._data = model

    def delete(self, model: Status):
        pass
