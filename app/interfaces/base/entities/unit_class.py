"""
    Base UnitClass class implementation
"""

from dataclasses import dataclass

from app.interfaces import abstract
from .skill import Skill


@dataclass
class UnitClass(abstract.UnitClass):
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill
