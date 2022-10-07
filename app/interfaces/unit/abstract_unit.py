"""
    Abstract class Unit
"""

from abc import ABC, abstractmethod

from ..weapon import BaseWeapon as Weapon
from ..armor import BaseArmor as Armor


class AbstractUnit(ABC):

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
    def is_alive(self):
        pass

    @property
    @abstractmethod
    def stamina_points(self):
        pass

    @stamina_points.setter
    @abstractmethod
    def stamina_points(self, value: float):
        pass

    @abstractmethod
    def equip_weapon(self, weapon: Weapon):
        pass

    @abstractmethod
    def equip_armor(self, armor: Armor):
        pass

    @property
    @abstractmethod
    def defence(self) -> float:
        pass

    @property
    @abstractmethod
    def damage(self) -> float:
        pass

    @abstractmethod
    def _count_damage(self, target) -> float:
        pass

    @abstractmethod
    def get_damage(self, damage: float):
        pass

    @abstractmethod
    def hit(self, target):
        pass

    @abstractmethod
    def use_skill(self, target):
        pass

    @abstractmethod
    def skip_turn(self, target):
        pass
