"""
    Abstract class EquipmentData
"""

from abc import ABC
from typing import Sequence

from .weapon import Weapon
from .armor import Armor


class EquipmentData(ABC):
    weapons: Sequence[Weapon] = NotImplemented
    armors: Sequence[Armor] = NotImplemented
