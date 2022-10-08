"""
    DAO abstraction level
    UnitClass DAO
"""

from typing import Optional, Type, List

from .base import BaseDAO
from .models import UnitClass
from app.game_container import unit_classes


class UnitClassDAO(BaseDAO[UnitClass]):
    __model__ = Type[UnitClass]
    _data = unit_classes

    def get_by_id(self, pk: int) -> Optional[UnitClass]:
        return None

    def get_all(self, page: Optional[int] = None) -> List[UnitClass]:
        return []

    def create(self, model: UnitClass):
        return None

    def update(self, model: UnitClass):
        return None

    def delete(self, model: UnitClass):
        return None

    def get_by_name(self, name: str) -> Optional[UnitClass]:
        unit_class_data = self._data.get(name, None)
        if unit_class_data is None:
            return None

        return UnitClass(
            id=0,
            name=unit_class_data.name,
            max_health=unit_class_data.max_health,
            max_stamina=unit_class_data.max_stamina,
            attack=unit_class_data.attack,
            stamina=unit_class_data.stamina,
            armor=unit_class_data.armor,
            skill=unit_class_data.skill,
        )

    def get_names(self) -> List[str]:
        return list(self._data.keys())
