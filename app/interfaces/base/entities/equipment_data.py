"""
    Base Armor class implementation
"""

import marshmallow
import marshmallow_dataclass
from dataclasses import dataclass, field
from typing import Sequence

from app.interfaces import abstract
from .weapon import Weapon
from .armor import Armor


@dataclass
class EquipmentData(abstract.EquipmentData):
    weapons: Sequence[Weapon] = field(default_factory=list)
    armors: Sequence[Armor] = field(default_factory=list)

    class Meta:
        unknown = marshmallow.EXCLUDE


EquipmentDataSchema = marshmallow_dataclass.class_schema(EquipmentData)
