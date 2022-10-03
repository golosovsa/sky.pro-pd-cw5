"""
    Abstract class Weapon
"""

from abc import ABC, abstractmethod


class Weapon(ABC):
    id: int = NotImplemented
    name: str = NotImplemented
    min_damage: float = NotImplemented
    max_damage: float = NotImplemented
    stamina_per_hit: float = NotImplemented

    @property
    @abstractmethod
    def damage(self):
        pass
