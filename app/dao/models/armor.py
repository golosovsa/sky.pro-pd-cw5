"""
    Armor model
"""

from dataclasses import dataclass

from app.interfaces.armor import BaseArmor
from app.setup.db.models import BaseWithID


@dataclass
class Armor(BaseWithID, BaseArmor):
    pass
