"""
    Base Equipment class implementation
"""

import json
from operator import attrgetter
from pathlib import Path
from typing import List, Optional
from marshmallow.exceptions import MarshmallowError

from app.interfaces import abstract
from .equipment_data import EquipmentData, EquipmentDataSchema
from .weapon import Weapon
from .armor import Armor


class Equipment(abstract.Equipment):

    def __init__(self, filename: str):
        self._equipment: EquipmentData = self._get_equipment_data(filename)

    def get_weapon(self, weapon_name: str) -> Optional[Weapon]:
        for weapon in self._equipment.weapons:
            if weapon.name == weapon_name:
                return weapon
        return None

    def get_armor(self, armor_name: str) -> Optional[Armor]:
        for armor in self._equipment.armors:
            if armor.name == armor_name:
                return armor
        return None

    def get_weapon_names(self) -> List[str]:
        return list(map(attrgetter("name"), self._equipment.weapons))

    def get_armor_names(self) -> List[str]:
        return list(map(attrgetter("name"), self._equipment.armors))

    @staticmethod
    def _get_equipment_data(filename: str) -> EquipmentData:
        try:
            path = Path(filename)
            with path.open("rt", encoding="utf-8") as fin:
                data = json.load(fin)
            return EquipmentDataSchema().load(data=data)
        except TypeError as error:
            raise ValueError(f"filename {filename} received a TypeError. " + str(error))
        except json.JSONDecodeError as error:
            raise ValueError(f"filename {filename} received a JSONDecodeError. " + str(error))
        except OSError as error:
            raise ValueError(f"filename {filename} received an IO error. " + str(error))
        except MarshmallowError as error:
            raise ValueError(f"filename {filename} received a MarshmallowError. " + str(error))
