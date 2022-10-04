"""
    Abstract class Equipment
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from .weapon import Weapon
from .armor import Armor
from .equipment_data import EquipmentData


class Equipment(ABC):

    @abstractmethod
    def get_weapon(self, weapon_name: str) -> Optional[Weapon]:
        pass

    @abstractmethod
    def get_armor(self, armor_name: str) -> Optional[Armor]:
        pass

    @abstractmethod
    def get_weapon_names(self) -> List[str]:
        pass

    @abstractmethod
    def get_armor_names(self) -> List[str]:
        pass

    @staticmethod
    @abstractmethod
    def _get_equipment_data(filename: str) -> EquipmentData:
        pass
