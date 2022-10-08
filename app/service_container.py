"""
    Service container implementation
"""

from app.dao import \
    WeaponDAO, \
    ArmorDAO, \
    UnitClassDAO, \
    BattleLogDAO, \
    PlayerDAO, \
    EnemyDAO

from app.services import \
    WeaponService, \
    ArmorService, \
    UnitClassService, \
    BattleLogService, \
    PlayerService, \
    EnemyService


# DAO
weapon_dao = WeaponDAO()
armor_dao = ArmorDAO()
unit_class_dao = UnitClassDAO()
battle_log_dao = BattleLogDAO()
player_dao = PlayerDAO()
enemy_dao = EnemyDAO()


# Services
weapon_service = WeaponService(weapon_dao)
armor_service = ArmorService(armor_dao)
unit_class_service = UnitClassService(unit_class_dao)
battle_log_service = BattleLogService(battle_log_dao)
player_service = PlayerService(player_dao)
enemy_service = EnemyService(enemy_dao)
