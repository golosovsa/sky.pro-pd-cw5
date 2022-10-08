"""
    Unit model
"""

from dataclasses import dataclass
from app.setup.db.models import BaseWithID


@dataclass
class Unit(BaseWithID):
    name: str
    health_points: float
    stamina_points: float
    unit_class: str
    weapon: str
    armor: str
