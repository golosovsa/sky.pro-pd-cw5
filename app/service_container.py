"""
    Service container implementation
"""

from app.dao import \
    WeaponDAO, \
    ArmorDAO, \
    UnitClassDAO, \
    BattleLogDAO

from app.services import \
    WeaponService, \
    ArmorService, \
    UnitClassService, \
    BattleLogService


# DAO
weapon_dao = WeaponDAO()
armor_dao = ArmorDAO()
unit_class_dao = UnitClassDAO()
battle_log_dao = BattleLogDAO()


# Services
weapon_service = WeaponService(weapon_dao)
armor_service = ArmorService(armor_dao)
unit_class_service = UnitClassService(unit_class_dao)
battle_log_service = BattleLogService(battle_log_dao)
