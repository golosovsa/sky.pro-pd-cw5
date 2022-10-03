"""
    Abstract class EquipmentData
"""

from abc import ABC
from typing import List

from .weapon import Weapon
from .armor import Armor


class EquipmentData(ABC):
    weapons: List[Weapon] = NotImplemented
    armors: List[Armor] = NotImplemented
