"""
    Abstract class UnitClass
"""

from abc import ABC
from .skill import Skill


class UnitClass(ABC):
    name: str = NotImplemented
    max_health: float = NotImplemented
    max_stamina: float = NotImplemented
    attack: float = NotImplemented
    stamina: float = NotImplemented
    armor: float = NotImplemented
    skill: Skill = NotImplemented
