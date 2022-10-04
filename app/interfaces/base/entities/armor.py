"""
    Base Armor class implementation
"""

import marshmallow
import marshmallow_dataclass
from dataclasses import dataclass

from app.interfaces import abstract


@dataclass
class Armor(abstract.Armor):
    id: int
    name: str
    defence: float
    stamina_per_turn: float

    class Meta:
        unknown = marshmallow.EXCLUDE


ArmorSchema = marshmallow_dataclass.class_schema(Armor)
