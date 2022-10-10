"""
    Service abstraction level
    Enemy service class
"""

from typing import List

from .base import BaseService
from app.dao import EnemyDAO


class EnemyService(BaseService[EnemyDAO]):
    _updatable_fields: List[str] = ["name", "unit_class", "weapon", "armor", ]

    def __init__(self, dao: EnemyDAO):
        super(EnemyService, self).__init__(dao)
        self._dao: EnemyDAO = dao

    def create_enemy(self, name, unit_class, weapon, armor) -> bool:
        return self._dao.create_enemy(name, unit_class, weapon, armor)
