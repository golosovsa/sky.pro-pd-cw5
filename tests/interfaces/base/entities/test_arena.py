"""
    Test base Arena
"""

from pytest import fixture

from app.interfaces import base


@fixture
def derived_arena_class():
    class DerivedArena(base.Arena):
        def _end_game(self):
            pass

    return DerivedArena


@fixture
def equipped_arena(derived_arena_class, equipped_unit_instance_1, equipped_unit_instance_2):
    derived_arena = derived_arena_class()
    derived_arena.start_game(equipped_unit_instance_1, equipped_unit_instance_2)
    return derived_arena


@fixture
def weapon_damage_1000():
    return base.Weapon(
        id=1000,
        name="1000 Damage",
        min_damage=1000.0,
        max_damage=1000.0,
        stamina_per_hit=1,
    )


@fixture
def class_damage_1000():
    return base.UnitClass(
        name="1000_DAMAGE_SKILL_CLASS",
        max_health=100.0,
        max_stamina=100.0,
        attack=5,
        stamina=5,
        armor=5,
        skill=base.Skill(
            name="1000 Damage Skill",
            stamina=1.0,
            damage=1000.0
        )
    )


class TestArena:

    def test_constructor(self, derived_arena_class):
        arena = derived_arena_class()
        assert not arena.is_game_start

    def test_started_arena(self, equipped_arena):
        assert equipped_arena.is_game_start

    def test_logs(self, equipped_arena):
        logs = []
        equipped_arena._player._log = lambda msg: logs.append(msg)
        equipped_arena._enemy._log = lambda msg: logs.append(msg)

        equipped_arena.make_a_player_hit()
        equipped_arena.make_next_turn()

        assert logs

    def test_player_win_after_hit(self, equipped_arena, weapon_damage_1000):
        equipped_arena._player._weapon = weapon_damage_1000
        assert not equipped_arena.is_game_end
        equipped_arena.make_a_player_hit()
        assert equipped_arena.is_game_end

    def test_enemy_win_after_hit(self, equipped_arena, weapon_damage_1000, class_damage_1000):
        equipped_arena._enemy._weapon = weapon_damage_1000
        equipped_arena._enemy._unit_class = class_damage_1000
        assert not equipped_arena.is_game_end
        equipped_arena.make_a_player_hit()
        assert not equipped_arena.is_game_end
        equipped_arena.make_next_turn()
        assert equipped_arena.is_game_end

    def test_use_player_skill(self, equipped_arena):
        assert not equipped_arena.is_game_end
        equipped_arena.use_player_skill()
        assert not equipped_arena.is_game_end

    def test_skip(self, equipped_arena):
        assert not equipped_arena.is_game_end
        equipped_arena.skip_turn()
        assert not equipped_arena.is_game_end
