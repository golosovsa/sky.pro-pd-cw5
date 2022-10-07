"""
    Base UnitClass class implementation
"""

from dataclasses import dataclass

from ..skill import BaseSkill as Skill


@dataclass
class BaseUnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill
