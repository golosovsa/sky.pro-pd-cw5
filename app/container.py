"""
    Service container implementation
"""

from app.constants import DATA_DIR
from app import interfaces

equipment = interfaces.Equipment(str(DATA_DIR / "equipment.json"))

unit_classes = {
    interfaces.WarriorClass.name: interfaces.WarriorClass,
    interfaces.ThiefClass.name: interfaces.ThiefClass,
}

units = {
    "player": interfaces.PlayerUnit,
    "enemy": interfaces.EnemyUnit,
}

Arena = interfaces.Arena
