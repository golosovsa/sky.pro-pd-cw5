"""
    Game container implementation
"""
from typing import Optional

from app import interfaces

Equipment = interfaces.Equipment

unit_classes = {
    interfaces.WarriorClass.name: interfaces.WarriorClass,
    interfaces.ThiefClass.name: interfaces.ThiefClass,
}

Arena = interfaces.Arena
BattleLog = interfaces.BattleLog


class Game:
    _equipment = None

    _player: Optional[interfaces.PlayerUnit] = None
    _enemy:  Optional[interfaces.EnemyUnit] = None

    _fight_result: str = "Еще не было ни одной игры"

    _screens = [
        "start_and_results",
        "create_player",
        "create_enemy",
        "fight",
    ]

    _current_screen_index = 0

    _arena: Optional[Arena] = None

    @property
    def player(self):
        return self._player

    @property
    def enemy(self):
        return self._enemy

    @property
    def screen(self):
        self._update_screen_index()
        return self._screens[self._current_screen_index]

    def _update_screen_index(self):
        if self._arena is None:
            self._current_screen_index = 0
            return
        if self._player is None:
            self._current_screen_index = 1
            return
        if self._enemy is None:
            self._current_screen_index = 2
            return
        if not self._arena.is_game_end:
            self._current_screen_index = 3
        self._current_screen_index = 2

    def start_game(self):
        if self._current_screen_index != 0:
            return

        self._equipment = Equipment("")
        self._arena = Arena()
        self._player = None
        self._enemy = None

    def select_player(self, name: str, class_name: str, armor_name: str, weapon_name: str):
        if self._current_screen_index != 1:
            return

        self._player = interfaces.PlayerUnit(
            name=name,
            unit_class=unit_classes[class_name]
        )

        if self._player is None or self._equipment is None:
            return

        self._player.equip_armor(self._equipment.get_armor(armor_name))
        self._player.equip_weapon(self._equipment.get_weapon(weapon_name))

    def select_enemy(self, name: str, class_name: str, armor_name: str, weapon_name: str):
        if self._current_screen_index != 2:
            return

        self._enemy = interfaces.EnemyUnit(
            name=name,
            unit_class=unit_classes[class_name]
        )

        if self._enemy is None or self._equipment is None:
            return

        self._enemy.equip_armor(self._equipment.get_armor(armor_name=armor_name))
        self._enemy.equip_weapon(self._equipment.get_weapon(weapon_name=weapon_name))

        self._arena.start_game(self._player, self._enemy)

    def _end_game(self):
        self._fight_result = self._arena.battle_result
        self._arena = None

    def fight(self, action: str):
        if self._current_screen_index != 3 or self._arena is None:
            return

        if action == "hit":
            self._arena.make_a_player_hit()
        elif action == "skill":
            self._arena.use_player_skill()
        elif action == "skip":
            self._arena.skip_turn()
        else:
            return

        # match action:
        #     case "hit":
        #         self._arena.make_a_player_hit()
        #     case "skill":
        #         self._arena.use_player_skill()
        #     case "skip":
        #         self._arena.skip_turn()
        #     case _:
        #         return

        if self._arena.is_game_end:
            self._end_game()

        self._arena.make_next_turn()

        if self._arena.is_game_end:
            self._end_game()


game = Game()
