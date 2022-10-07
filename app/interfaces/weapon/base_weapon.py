"""
    Base Weapon class implementation
"""

import marshmallow
import marshmallow_dataclass
from dataclasses import dataclass
from random import uniform

from .abstract_weapon import AbstractWeapon


@dataclass
class BaseWeapon(AbstractWeapon):
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


BaseWeaponSchema = marshmallow_dataclass.class_schema(BaseWeapon)
