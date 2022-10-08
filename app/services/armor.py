"""
    Service abstraction level
    Armor service class
"""

from .base import BaseService
from app.dao import ArmorDAO


class ArmorService(BaseService[ArmorDAO]):
    _updatable_fields = ["name", "defence", "stamina_per_turn", ]

    def __init__(self, dao: ArmorDAO):
        super().__init__(dao)
        self._dao: ArmorDAO = dao

    def get_names(self):
        return self._dao.get_names()

    def get_by_name(self, name: str):
        return self._dao.get_by_name(name)
