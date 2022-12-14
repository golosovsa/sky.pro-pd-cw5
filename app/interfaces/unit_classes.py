"""
    Module class container for base class UnitClass
"""

from .unit_class import BaseUnitClass as UnitClass
from .skills import HardShot, FuryPunch


WarriorClass = UnitClass(
    name="Воин",
    max_health=60,
    max_stamina=30,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=HardShot()
)


ThiefClass = UnitClass(
    name="Вор",
    max_health=50,
    max_stamina=25,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=FuryPunch()
)
