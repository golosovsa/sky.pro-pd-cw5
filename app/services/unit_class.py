"""
    Service abstraction level
    UnitClass service class
"""

from .base import BaseService
from app.dao import UnitClassDAO


class UnitClassService(BaseService[UnitClassDAO]):
    _updatable_fields = ["name", "max_health", "max_stamina", "attack", "stamina", "armor", "skill", ]

    def __init__(self, dao: UnitClassDAO):
        super().__init__(dao)
        self._dao: UnitClassDAO = dao

    def get_names(self):
        return self._dao.get_names()

    def get_by_name(self, name: str):
        return self._dao.get_by_name(name)
