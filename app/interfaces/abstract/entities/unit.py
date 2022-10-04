"""
    Abstract class Unit
"""

from abc import ABC, abstractmethod
from typing import Optional, TypeVar

from .unit_class import UnitClass

from .weapon import Weapon
from .armor import Armor

TUnit = TypeVar("TUnit", bound="Unit")


class Unit(ABC):
    _name: str = NotImplemented
    _unit_class: UnitClass = NotImplemented
    _hp: float = NotImplemented
    _stamina: float = NotImplemented
    _weapon: Weapon = NotImplemented
    _armor: Armor = NotImplemented
    _is_skill_used: bool = NotImplemented

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def health_points(self):
        pass

    @property
    @abstractmethod
    def stamina_points(self):
        pass

    @stamina_points.setter
    @abstractmethod
    def stamina_points(self, value):
        pass

    @abstractmethod
    def equip_weapon(self, weapon: Weapon):
        pass

    @abstractmethod
    def equip_armor(self, armor: Armor):
        pass

    @abstractmethod
    def _count_damage(self, target: TUnit) -> int:
        pass

    @abstractmethod
    def get_damage(self, damage: float) -> Optional[int]:
        pass

    @abstractmethod
    def hit(self, target: TUnit) -> str:
        pass

    @abstractmethod
    def use_skill(self, target: TUnit) -> str:
        pass
