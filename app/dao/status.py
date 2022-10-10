"""
    DAO abstraction level
    Status DAO
"""

from typing import Optional, List, Type

from .base import BaseDAO
from .models import Status
from app.game_container import game, Game


class StatusDAO(BaseDAO[Status]):
    __model__: Type[Status] = Status
    _data: Game = game

    def get_by_id(self, pk: int) -> Optional[Status]:
        return Status(
            id=0,
            user_pk=0,
            current_screen=game.screen,
            fight_result=game.fight_result,
        )

    def get_all(self, page: Optional[int] = None) -> List[Status]:
        pass

    def create(self, model: Status):
        pass

    def update(self, model: Status):
        pass

    def delete(self, model: Status):
        pass
