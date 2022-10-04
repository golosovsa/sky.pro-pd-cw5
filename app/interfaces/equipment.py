"""
    Class Equipment implementation
"""
from typing import TYPE_CHECKING

from app.interfaces import base

if TYPE_CHECKING:
    ABCSingletonEquipmentMeta = type
else:
    class ABCSingletonEquipmentMeta(base.SingletonMeta, type(base.Equipment)):
        pass


class Equipment(base.Equipment, metaclass=ABCSingletonEquipmentMeta):
    pass
