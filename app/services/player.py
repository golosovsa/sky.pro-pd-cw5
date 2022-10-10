"""
    Service abstraction level
    Player service class
"""

from .base import BaseService
from app.dao import PlayerDAO


class PlayerService(BaseService[PlayerDAO]):
    _updatable_fields = ["name", "unit_class", "weapon", "armor", ]

    def __init__(self, dao: PlayerDAO):
        super(PlayerService, self).__init__(dao)
        self._dao: PlayerDAO = dao

    def create_player(self, name, unit_class, weapon, armor) -> bool:
        return self._dao.create_player(name, unit_class, weapon, armor)
