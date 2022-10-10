"""
    DAO abstraction level
    Player DAO
"""

from typing import Type, Optional, List

from .base import BaseDAO
from .models import Unit
from app.game_container import Game, game


class PlayerDAO(BaseDAO[Unit]):
    __model__: Type[Unit] = Unit
    _data: Game = game

    def get_by_id(self, pk: int) -> Optional[Unit]:
        player = self._data.player

        if player is None:
            return None

        return self.__model__(
            id=0,
            name=player.name,
            health_points=player.health_points,
            stamina_points=player.stamina_points,
            unit_class=player.unit_class,
            weapon=player.weapon,
            armor=player.armor,
        )

    def get_all(self, page: Optional[int] = None) -> List[Unit]:
        return []

    def create(self, model: Unit):
        return None

    def update(self, model: Unit):
        return None

    def delete(self, model: Unit):
        return None

    def create_player(self, name, unit_class, weapon, armor) -> bool:
        try:
            self._data.select_player(name=name, class_name=unit_class, weapon_name=weapon, armor_name=armor)
            return True
        except RuntimeError:
            return False
