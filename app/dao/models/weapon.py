"""
    Weapon model
"""

from dataclasses import dataclass

from app.interfaces.weapon import BaseWeapon
from app.setup.db.models import BaseWithID


@dataclass
class Weapon(BaseWithID, BaseWeapon):
    pass
