"""
    Base Armor class implementation
"""

import marshmallow
import marshmallow_dataclass
from dataclasses import dataclass


@dataclass
class BaseArmor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float

    class Meta:
        unknown = marshmallow.EXCLUDE


BaseArmorSchema = marshmallow_dataclass.class_schema(BaseArmor)
