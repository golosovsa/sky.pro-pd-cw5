from pytest import fixture
from app.interfaces import base


@fixture
def derived_skill():
    class DerivedSkill(base.Skill):
        _name = "Derived"
        _stamina = 10.0
        _damage = 10.0

    return DerivedSkill


@fixture
def derived_unit():
    class DerivedUnit(base.Unit):

        def _log(self, message: str):
            pass

    return DerivedUnit


@fixture
def derived_skill_instance(derived_skill):
    return derived_skill()


@fixture
def derived_unit_instance_1(derived_unit, derived_skill_instance):
    return derived_unit(
        name="Derived_Unit_1",
        unit_class=base.UnitClass(
            name="Derived_Unit_Class_1",
            max_health=100.0,
            max_stamina=100.0,
            attack=5.0,
            stamina=5.0,
            armor=5.0,
            skill=derived_skill_instance
        )
    )


@fixture
def derived_unit_instance_2(derived_unit, derived_skill_instance):
    return derived_unit(
        name="Derived_Unit_2",
        unit_class=base.UnitClass(
            name="Derived_Unit_Class_2",
            max_health=100.0,
            max_stamina=100.0,
            attack=5.0,
            stamina=5.0,
            armor=5.0,
            skill=derived_skill_instance
        )
    )


@fixture
def derived_unit_instance_low_stamina(derived_unit, derived_skill_instance):
    return derived_unit(
        name="Derived_Unit_Low_Stamina",
        unit_class=base.UnitClass(
            name="Derived_Unit_Class_Low_Stamina",
            max_health=100.0,
            max_stamina=0.0,
            attack=5.0,
            stamina=5.0,
            armor=5.0,
            skill=derived_skill_instance
        )
    )


@fixture
def equipped_unit_instance_1(derived_unit_instance_1, equipment_object):
    armor = equipment_object.get_armor("кожаная броня")
    weapon = equipment_object.get_weapon("ножик")
    derived_unit_instance_1.equip_weapon(weapon)
    derived_unit_instance_1.equip_armor(armor)
    return derived_unit_instance_1


@fixture
def equipped_unit_instance_2(derived_unit_instance_2, equipment_object):
    armor = equipment_object.get_armor("кожаная броня")
    weapon = equipment_object.get_weapon("ножик")
    derived_unit_instance_2.equip_weapon(weapon)
    derived_unit_instance_2.equip_armor(armor)
    return derived_unit_instance_2


@fixture
def equipped_unit_instance_low_stamina(derived_unit_instance_low_stamina, equipment_object):
    armor = equipment_object.get_armor("кожаная броня")
    weapon = equipment_object.get_weapon("ножик")
    derived_unit_instance_low_stamina.equip_weapon(weapon)
    derived_unit_instance_low_stamina.equip_armor(armor)
    return derived_unit_instance_low_stamina
