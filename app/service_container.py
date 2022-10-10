"""
    Service container implementation
"""

from app.dao import \
    WeaponDAO, \
    ArmorDAO, \
    UnitClassDAO, \
    BattleLogDAO, \
    PlayerDAO, \
    EnemyDAO, \
    StatusDAO, \
    GameDAO, \
    FightDAO

from app.services import \
    WeaponService, \
    ArmorService, \
    UnitClassService, \
    BattleLogService, \
    PlayerService, \
    EnemyService, \
    StatusService, \
    GameService, \
    FightService


# DAO
weapon_dao = WeaponDAO()
armor_dao = ArmorDAO()
unit_class_dao = UnitClassDAO()
battle_log_dao = BattleLogDAO()
player_dao = PlayerDAO()
enemy_dao = EnemyDAO()
status_dao = StatusDAO()
game_dao = GameDAO()
fight_dao = FightDAO()


# Services
weapon_service = WeaponService(weapon_dao)
armor_service = ArmorService(armor_dao)
unit_class_service = UnitClassService(unit_class_dao)
battle_log_service = BattleLogService(battle_log_dao)
player_service = PlayerService(player_dao)
enemy_service = EnemyService(enemy_dao)
status_service = StatusService(status_dao)
game_service = GameService(game_dao)
fight_service = FightService(fight_dao)
