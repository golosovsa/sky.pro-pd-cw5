"""
    Service container implementation
"""

from app.dao import WeaponDAO, ArmorDAO

from app.services import WeaponService, ArmorService


# DAO
weapon_dao = WeaponDAO()
armor_dao = ArmorDAO()


# Services
weapon_service = WeaponService(weapon_dao)
armor_service = ArmorService(armor_dao)
