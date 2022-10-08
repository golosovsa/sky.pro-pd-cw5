"""
    Service container implementation
"""

from app.dao import WeaponDAO, ArmorDAO, UnitClassDAO

from app.services import WeaponService, ArmorService, UnitClassService


# DAO
weapon_dao = WeaponDAO()
armor_dao = ArmorDAO()
unit_class_dao = UnitClassDAO()


# Services
weapon_service = WeaponService(weapon_dao)
armor_service = ArmorService(armor_dao)
unit_class_service = UnitClassService(unit_class_dao)
