"""
    Class Skills implementation
"""

from .skill import BaseSkill as Skill


class FuryPunch(Skill):
    _name: str = "Свирепый пинок"
    _stamina: float = 6.0
    _damage: float = 12.0


class HardShot(Skill):
    _name: str = "Мощный укол"
    _stamina: float = 5.0
    _damage: float = 15.0
