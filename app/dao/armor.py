"""
    DAO abstraction level
    Armor DAO
"""

from typing import Optional, List, Type

from .base import BaseDAO
from .models import Armor
from app.game_container import Equipment


class ArmorDAO(BaseDAO[Armor]):
    __model__: Type[Armor] = Armor
    _data: Type[Equipment] = Equipment

    def get_by_id(self, pk: int) -> Optional[Armor]:
        return None

    def get_all(self, page: Optional[int] = None) -> List[Armor]:
        return []

    def create(self, model: Armor):
        return None

    def update(self, model: Armor):
        return None

    def delete(self, model: Armor):
        return None

    def get_by_name(self, name: str) -> Optional[Armor]:
        armor_data = self._data("").get_armor(name)
        if armor_data is None:
            return None
        return Armor(
            id=armor_data.id if armor_data.id is not None else 0,
            name=armor_data.name,
            defence=armor_data.defence,
            stamina_per_turn=armor_data.stamina_per_turn,
        )

    def get_names(self) -> List[str]:
        return self._data("").get_armor_names()
