"""
    Test Equipment base implementation
"""
import pytest
from dataclasses import asdict

from app.interfaces.base import Equipment, EquipmentData, Armor, Weapon


class TestEquipment:

    def test_get_equipment_data(self, equipment_data, equipment_file):
        loaded_data: EquipmentData = Equipment._get_equipment_data(equipment_file)
        assert loaded_data.armors
        assert loaded_data.weapons
        fixture_armors_content = [set(item.values()) for item in equipment_data["armors"]]
        fixture_weapons_content = [set(item.values()) for item in equipment_data["weapons"]]
        for armor in loaded_data.armors:
            content = set(asdict(armor).values())
            assert content in fixture_armors_content
        for weapon in loaded_data.weapons:
            content = set(asdict(weapon).values())
            assert content in fixture_weapons_content

    def test_get_equipment_data_errors(self):
        with pytest.raises(ValueError):
            equipment = Equipment._get_equipment_data("None")

    def test_constructor(self, equipment_file):
        equipment = Equipment(equipment_file)
        assert equipment._equipment
        assert type(equipment._equipment) == EquipmentData

    def test_get_weapon(self, equipment_data, equipment_file):
        equipment = Equipment(equipment_file)
        for weapon_data in equipment_data["weapons"]:
            weapon = equipment.get_weapon(weapon_data["name"])
            assert weapon
            assert type(weapon) == Weapon
            assert weapon.id == weapon_data["id"]
            assert weapon.max_damage == weapon_data["max_damage"]
            assert weapon.min_damage == weapon_data["min_damage"]
            assert weapon.stamina_per_hit == weapon_data["stamina_per_hit"]

    def test_get_armor(self, equipment_data, equipment_file):
        equipment = Equipment(equipment_file)
        for armor_data in equipment_data["armors"]:
            armor = equipment.get_armor(armor_data["name"])
            assert armor
            assert type(armor) == Armor
            assert armor.id == armor_data["id"]
            assert armor.defence == armor_data["defence"]
            assert armor.stamina_per_turn == armor_data["stamina_per_turn"]

    def test_get_weapon_names(self, equipment_data, equipment_file):
        names_data = [item["name"] for item in equipment_data["weapons"]]
        equipment = Equipment(equipment_file)
        names = equipment.get_weapon_names()
        assert names
        assert type(names) == list
        assert len(names) == len(names_data)
        for name in names:
            assert name in names_data

    def test_get_armor_names(self, equipment_data, equipment_file):
        names_data = [item["name"] for item in equipment_data["armors"]]
        equipment = Equipment(equipment_file)
        names = equipment.get_armor_names()
        assert names
        assert type(names) == list
        assert len(names) == len(names_data)
        for name in names:
            assert name in names_data
