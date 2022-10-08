"""
    Service abstraction level
    Weapon service class
"""

from .base import BaseService
from app.dao import WeaponDAO


class WeaponService(BaseService[WeaponDAO]):
    _updatable_fields = ["name", "min_damage", "max_damage", "stamina_per_hit", ]

    def __init__(self, dao: WeaponDAO):
        super().__init__(dao)
        self._dao: WeaponDAO = dao

    def get_names(self):
        return self._dao.get_names()

    def get_by_name(self, name: str):
        return self._dao.get_by_name(name)
