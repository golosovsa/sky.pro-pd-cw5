"""
    DAO abstraction level
    Fight DAO
"""

from typing import Type, Optional, List

from .base import BaseDAO
from app.game_container import Game, game


class FightDAO(BaseDAO[None]):
    __model__: Type[None] = type(None)
    _data: Game = game

    def get_by_id(self, pk: int) -> Optional[None]:
        pass

    def get_all(self, page: Optional[int] = None) -> List[None]:
        return []

    def create(self, model: None):
        return None

    def update(self, model: None):
        return None

    def delete(self, model: None):
        return None

    def fight(self, action):
        try:
            self._data.fight(action)
            return True
        except RuntimeError:
            return False
