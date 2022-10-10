"""
    DAO abstraction level
    Enemy DAO
"""

from typing import Type, Optional, List

from .base import BaseDAO
from .models import Unit
from app.game_container import Game, game


class EnemyDAO(BaseDAO[Unit]):
    __model__: Type[Unit] = Unit
    _data: Game = game

    def get_by_id(self, pk: int) -> Optional[Unit]:
        enemy = self._data.enemy

        if enemy is None:
            return None

        return self.__model__(
            id=0,
            name=enemy.name,
            health_points=enemy.health_points,
            stamina_points=enemy.stamina_points,
            unit_class=enemy.unit_class,
            weapon=enemy.weapon,
            armor=enemy.armor,
        )

    def get_all(self, page: Optional[int] = None) -> List[Unit]:
        return []

    def create(self, model: Unit):
        return None

    def update(self, model: Unit):
        return None

    def delete(self, model: Unit):
        return None

    def create_enemy(self, name, unit_class, weapon, armor) -> bool:
        try:
            self._data.select_enemy(name=name, class_name=unit_class, weapon_name=weapon, armor_name=armor)
            return True
        except RuntimeError:
            return False
