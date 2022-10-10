"""
    Service abstraction level
    Game service class
"""

from typing import List

from .base import BaseService
from app.dao import GameDAO


class GameService(BaseService[GameDAO]):
    _updatable_fields: List[str] = []

    def __init__(self, dao: GameDAO):
        super(GameService, self).__init__(dao)
        self._dao: GameDAO = dao

    def start_game(self):
        return self._dao.start_game()
