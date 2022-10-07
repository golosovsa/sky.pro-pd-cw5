"""
    Base Armor class implementation
"""

import marshmallow
import marshmallow_dataclass
from dataclasses import dataclass, field
from typing import Sequence

from ..weapon import BaseWeapon as Weapon
from ..armor import BaseArmor as Armor


@dataclass
class BaseEquipmentData:
    weapons: Sequence[Weapon] = field(default_factory=list)
    armors: Sequence[Armor] = field(default_factory=list)

    class Meta:
        unknown = marshmallow.EXCLUDE


BaseEquipmentDataSchema = marshmallow_dataclass.class_schema(BaseEquipmentData)
