"""
    Game container implementation
"""

from app import interfaces

Equipment = interfaces.Equipment

unit_classes = {
    interfaces.WarriorClass.name: interfaces.WarriorClass,
    interfaces.ThiefClass.name: interfaces.ThiefClass,
}

units = {
    "player": interfaces.PlayerUnit,
    "enemy": interfaces.EnemyUnit,
}

Arena = interfaces.Arena
BattleLog = interfaces.BattleLog
