"""
    UnitClass model
"""

from dataclasses import dataclass

from app.interfaces.unit_class import BaseUnitClass
from app.setup.db.models import BaseWithID


@dataclass
class UnitClass(BaseWithID, BaseUnitClass):
    pass
