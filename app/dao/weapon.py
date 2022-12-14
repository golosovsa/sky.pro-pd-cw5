"""
    DAO abstraction level
    Weapon DAO
"""

from typing import Optional, List, Type

from .base import BaseDAO
from .models import Weapon
from app.game_container import Equipment


class WeaponDAO(BaseDAO[Weapon]):
    __model__: Type[Weapon] = Weapon
    _data: Type[Equipment] = Equipment

    def get_by_id(self, pk: int) -> Optional[Weapon]:
        return None

    def get_all(self, page: Optional[int] = None) -> List[Weapon]:
        return []

    def create(self, model: Weapon):
        return None

    def update(self, model: Weapon):
        return None

    def delete(self, model: Weapon):
        return None

    def get_by_name(self, name: str) -> Optional[Weapon]:
        weapon_data = self._data("").get_weapon(name)
        if weapon_data is None:
            return None
        return Weapon(
            id=weapon_data.id if weapon_data.id is not None else 0,
            name=weapon_data.name,
            min_damage=weapon_data.min_damage,
            max_damage=weapon_data.max_damage,
            stamina_per_hit=weapon_data.stamina_per_hit,
        )

    def get_names(self) -> List[str]:
        return self._data("").get_weapon_names()
