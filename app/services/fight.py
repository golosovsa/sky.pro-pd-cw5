"""
    Service abstraction level
    Fight service class
"""

from typing import List

from .base import BaseService
from app.dao import FightDAO


class FightService(BaseService[FightDAO]):
    _updatable_fields: List[str] = []

    def __init__(self, dao: FightDAO):
        super(FightService, self).__init__(dao)
        self._dao: FightDAO = dao

    def fight(self, action: str):
        return self._dao.fight(action)
