""""
    Service abstraction level
    Base service class
"""

from typing import TypeVar, Generic, Optional, List, Any, Dict

from app.dao.base import BaseDAO
from app.setup.db.models import Base
from app.exceptions import ItemNotFound, InvalidDataContent


T = TypeVar("T", bound=BaseDAO)


class BaseService(Generic[T]):
    _updatable_fields: List[str] = []

    def __init__(self, dao: BaseDAO):
        self._dao = dao

    def _check_data(self, data: Dict[str, Any]):
        if len(self._updatable_fields) != len(data):
            return False
        for field in self._updatable_fields:
            if field not in data:
                return False
        return True

    def _check_partially_data(self, data: Dict[str, Any]):
        for field in data:
            if field not in self._updatable_fields:
                return False
        return True

    def get_item(self, pk: int) -> Optional[Base]:
        if model := self._dao.get_by_id(pk):
            return model
        raise ItemNotFound("Item not found.")

    def get_all(self, page: Optional[int] = None) -> List[Base]:
        """ Get list of models """
        return self._dao.get_all(page=page)

    def create(self, data: Dict[str, Any]) -> Base:
        if not self._check_data(data):
            raise InvalidDataContent("Invalid data content.")
        model = self._dao.create(self._dao.__model__(**data))
        return model

    def update(self, pk: int, data: Dict[str, Any]) -> Base:
        if not self._check_data(data):
            raise InvalidDataContent("Invalid data content.")
        model = self.get_item(pk)
        for field in self._updatable_fields:
            setattr(model, field, data[field])

        return self._dao.create(model)

    def partially_update(self, pk: int, data: Dict[str, Any]) -> Base:
        if not self._check_partially_data(data):
            raise InvalidDataContent("Invalid data content.")
        model = self.get_item(pk)
        for field in self._updatable_fields:
            if field in data:
                setattr(model, field, data[field])

        return self._dao.update(model)

    def delete(self, pk: int):
        model = self._dao.get_by_id(pk)
        self._dao.delete(model)
