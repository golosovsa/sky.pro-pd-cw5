"""
    Base Weapon class implementation
"""

import marshmallow
import marshmallow_dataclass
from dataclasses import dataclass
from random import uniform

from app.interfaces import abstract


@dataclass
class Weapon(abstract.Weapon):
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    class Meta:
        unknown = marshmallow.EXCLUDE

    @property
    def damage(self):
        return uniform(self.min_damage, self.max_damage)


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)
