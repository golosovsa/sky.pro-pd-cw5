"""
    Test base Unit
"""

from app.interfaces.unit_class import BaseUnitClass as UnitClass


class TestUnit:

    def test_constructor(self, derived_unit, derived_skill):
        derived = derived_unit(
            name="Derived_Unit",
            unit_class=UnitClass(
                name="Derived_Unit_Class_1",
                max_health=100.0,
                max_stamina=100.0,
                attack=5.0,
                stamina=5.0,
                armor=5.0,
                skill=derived_skill()
            )
        )
        assert derived.health_points == 100.0
        assert derived.stamina_points == 100.0

    def test_unit_defence_without_armor(self, derived_unit_instance_1):
        assert derived_unit_instance_1.defence == 0

    def test_unit_defence_with_low_stamina(self, equipped_unit_instance_low_stamina):
        assert equipped_unit_instance_low_stamina.defence == 0

    def test_unit_defence_with_armor(self, equipped_unit_instance_1, equipment_object):
        assert equipped_unit_instance_1.defence != 0
        defence = \
            equipped_unit_instance_1._armor.defence * \
            equipped_unit_instance_1._unit_class.armor
        assert abs(equipped_unit_instance_1.defence - defence) < equipped_unit_instance_1._EPSILON

    def test_unit_damage_without_weapon(self, derived_unit_instance_1):
        assert derived_unit_instance_1.damage == 0

    def test_unit_damage_with_low_stamina(self, equipped_unit_instance_low_stamina):
        assert equipped_unit_instance_low_stamina.damage == 0

    def test_unit_damage_with_weapon(self, equipped_unit_instance_1):
        damage = equipped_unit_instance_1.damage
        min_damage = \
            equipped_unit_instance_1._weapon.min_damage * \
            equipped_unit_instance_1._unit_class.attack - \
            equipped_unit_instance_1._EPSILON
        max_damage = \
            equipped_unit_instance_1._weapon.max_damage * \
            equipped_unit_instance_1._unit_class.attack + \
            equipped_unit_instance_1._EPSILON
        assert damage != 0
        assert min_damage <= damage <= max_damage

    def test_get_zero_damage(self, equipped_unit_instance_1):
        stamina = equipped_unit_instance_1.stamina_points
        regenerate = equipped_unit_instance_1._STAMINA_PER_TURN * equipped_unit_instance_1._unit_class.stamina
        stamina_consumption = equipped_unit_instance_1._armor.stamina_per_turn
        damage = equipped_unit_instance_1.get_damage(0)
        assert equipped_unit_instance_1.stamina_points > stamina
        assert abs(
            equipped_unit_instance_1.stamina_points -
            stamina -
            regenerate +
            stamina_consumption
        ) < equipped_unit_instance_1._EPSILON
        assert damage == 0

    def test_get_damage_without_armor(self, derived_unit_instance_1):
        stamina = derived_unit_instance_1.stamina_points
        regenerate = derived_unit_instance_1._STAMINA_PER_TURN * derived_unit_instance_1._unit_class.stamina
        damage = derived_unit_instance_1.get_damage(10.0)
        assert derived_unit_instance_1.stamina_points > stamina
        assert abs(derived_unit_instance_1.stamina_points - stamina - regenerate) < derived_unit_instance_1._EPSILON
        assert damage == 10.0

    def test_get_damage_with_armor(self, equipped_unit_instance_1):
        stamina = equipped_unit_instance_1.stamina_points
        stamina_consumption = equipped_unit_instance_1._armor.stamina_per_turn
        regenerate = equipped_unit_instance_1._STAMINA_PER_TURN * equipped_unit_instance_1._unit_class.stamina
        damage = equipped_unit_instance_1.get_damage(10.0)
        assert equipped_unit_instance_1.stamina_points > stamina
        assert abs(
            equipped_unit_instance_1.stamina_points -
            stamina -
            regenerate +
            stamina_consumption) < equipped_unit_instance_1._EPSILON
        assert damage == 10.0

    def test_hit_attack_hp(self, equipped_unit_instance_1, equipped_unit_instance_2):
        hp_unit_before_1 = equipped_unit_instance_1.health_points
        equipped_unit_instance_1.hit(equipped_unit_instance_2)

        assert hp_unit_before_1 == equipped_unit_instance_1.health_points

    def test_hit_attack_stamina(self, equipped_unit_instance_1, equipped_unit_instance_2):
        stamina_unit_before_1 = equipped_unit_instance_1.stamina_points
        equipped_unit_instance_1.hit(equipped_unit_instance_2)

        stamina_consumption = equipped_unit_instance_1._weapon.stamina_per_hit
        stamina_regeneration = \
            equipped_unit_instance_1._STAMINA_PER_TURN * \
            equipped_unit_instance_1._unit_class.stamina

        assert abs(
            equipped_unit_instance_1.stamina_points -
            stamina_unit_before_1 +
            stamina_consumption -
            stamina_regeneration
        ) < equipped_unit_instance_1._EPSILON

    def test_hit_defender_hp(self, equipped_unit_instance_1, equipped_unit_instance_2):
        hp_unit_before_2 = equipped_unit_instance_2.health_points
        equipped_unit_instance_1.hit(equipped_unit_instance_2)
        min_damage = \
            equipped_unit_instance_1._weapon.min_damage * \
            equipped_unit_instance_1._unit_class.attack - \
            equipped_unit_instance_1._EPSILON
        max_damage = \
            equipped_unit_instance_1._weapon.max_damage * \
            equipped_unit_instance_1._unit_class.attack + \
            equipped_unit_instance_1._EPSILON
        defence = equipped_unit_instance_2._armor.defence * equipped_unit_instance_2._unit_class.armor
        min_damage -= defence
        max_damage -= defence
        min_damage = min_damage if min_damage > 0 else 0
        max_damage = max_damage if max_damage > 0 else 0
        damage = hp_unit_before_2 - equipped_unit_instance_2.health_points
        assert min_damage <= damage <= max_damage

    def test_hit_defender_stamina(self, equipped_unit_instance_1, equipped_unit_instance_2):
        stamina_unit_before_2 = equipped_unit_instance_2.stamina_points
        equipped_unit_instance_1.hit(equipped_unit_instance_2)

        stamina_consumption = equipped_unit_instance_2._armor.stamina_per_turn
        stamina_regeneration = \
            equipped_unit_instance_2._STAMINA_PER_TURN * \
            equipped_unit_instance_2._unit_class.stamina

        assert abs(
            equipped_unit_instance_2.stamina_points -
            stamina_unit_before_2 +
            stamina_consumption -
            stamina_regeneration
        ) < equipped_unit_instance_2._EPSILON

    def test_use_skill_attack_hp(self, equipped_unit_instance_1, equipped_unit_instance_2):
        hp_unit_before_1 = equipped_unit_instance_1.health_points
        equipped_unit_instance_1.use_skill(equipped_unit_instance_2)

        assert hp_unit_before_1 == equipped_unit_instance_1.health_points

    def test_use_skill_attack_stamina(self, equipped_unit_instance_1, equipped_unit_instance_2):
        # equipped_unit_instance_1._log = lambda msg: print(msg)
        # equipped_unit_instance_2._log = lambda msg: print(msg)
        stamina_unit_before_1 = equipped_unit_instance_1.stamina_points
        equipped_unit_instance_1.use_skill(equipped_unit_instance_2)
        stamina_consumption = equipped_unit_instance_1._unit_class.skill.stamina
        stamina_regeneration = \
            equipped_unit_instance_1._STAMINA_PER_TURN * \
            equipped_unit_instance_1._unit_class.stamina

        assert abs(
            equipped_unit_instance_1.stamina_points -
            stamina_unit_before_1 +
            stamina_consumption -
            stamina_regeneration
        ) < equipped_unit_instance_2._EPSILON

    def test_use_skill_defender_hp(self, equipped_unit_instance_1, equipped_unit_instance_2):
        hp_unit_before_2 = equipped_unit_instance_2.health_points
        equipped_unit_instance_1.use_skill(equipped_unit_instance_2)
        damage = equipped_unit_instance_1._unit_class.skill.damage
        defence = equipped_unit_instance_2._armor.defence * equipped_unit_instance_2._unit_class.armor
        damage -= defence
        damage = damage if damage > 0 else 0
        damage_after_skill = hp_unit_before_2 - equipped_unit_instance_2.health_points

        assert abs(damage_after_skill - damage) < equipped_unit_instance_1._EPSILON

    def test_use_skill_defender_stamina(self, equipped_unit_instance_1, equipped_unit_instance_2):
        stamina_unit_before_2 = equipped_unit_instance_2.stamina_points
        equipped_unit_instance_1.use_skill(equipped_unit_instance_2)
        stamina_consumption = equipped_unit_instance_2._armor.stamina_per_turn
        stamina_regeneration = \
            equipped_unit_instance_2._STAMINA_PER_TURN * \
            equipped_unit_instance_2._unit_class.stamina

        assert abs(
            equipped_unit_instance_2.stamina_points -
            stamina_unit_before_2 +
            stamina_consumption -
            stamina_regeneration
        ) < equipped_unit_instance_2._EPSILON

    def test_skip_turn_attack_hp(self, equipped_unit_instance_1, equipped_unit_instance_2):
        hp_unit_before_1 = equipped_unit_instance_1.health_points
        equipped_unit_instance_1.skip_turn(equipped_unit_instance_2)

        assert hp_unit_before_1 == equipped_unit_instance_1.health_points

    def test_skip_turn_attack_stamina(self, equipped_unit_instance_1, equipped_unit_instance_2):
        stamina_unit_before_1 = equipped_unit_instance_1.stamina_points
        equipped_unit_instance_1.skip_turn(equipped_unit_instance_2)
        stamina_regeneration = \
            equipped_unit_instance_1._STAMINA_PER_TURN * \
            equipped_unit_instance_1._unit_class.stamina

        assert abs(
            equipped_unit_instance_1.stamina_points -
            stamina_unit_before_1 -
            stamina_regeneration
        ) <= equipped_unit_instance_1._EPSILON

    def test_skip_turn_defender_hp(self, equipped_unit_instance_1, equipped_unit_instance_2):
        hp_unit_before_2 = equipped_unit_instance_2.health_points
        equipped_unit_instance_1.skip_turn(equipped_unit_instance_2)

        assert hp_unit_before_2 == equipped_unit_instance_2.health_points

    def test_skip_turn_defender_stamina(self, equipped_unit_instance_1, equipped_unit_instance_2):
        stamina_unit_before_2 = equipped_unit_instance_2.stamina_points
        equipped_unit_instance_1.skip_turn(equipped_unit_instance_2)

        assert stamina_unit_before_2 == equipped_unit_instance_2.stamina_points
