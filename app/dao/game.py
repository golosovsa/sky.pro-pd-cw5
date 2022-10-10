"""
    DAO abstraction level
    Game DAO
"""

from typing import Type, Optional, List

from .base import BaseDAO
from app.game_container import Game, game


class GameDAO(BaseDAO[None]):
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

    def start_game(self) -> bool:
        try:
            self._data.start_game()
            return True
        except RuntimeError:
            return False
