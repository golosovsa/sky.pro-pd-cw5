"""
    Class Equipment Singleton implementation
"""

from typing import TYPE_CHECKING

from .equipment import BaseEquipment
from .singleton_meta import BaseSingletonMeta as SingletonMeta

if TYPE_CHECKING:
    ABCSingletonEquipmentMeta = type
else:
    class ABCSingletonEquipmentMeta(SingletonMeta, type(BaseEquipment)):
        pass


class Equipment(BaseEquipment, metaclass=ABCSingletonEquipmentMeta):

    def __init__(self, filename: str):
        super(Equipment, self).__init__(filename)
