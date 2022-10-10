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

    _fight_result: str = "Вы не играли еще ни одной игры"

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
    def fight_result(self):
        return self._fight_result

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
            return
        self._arena = None
        self._current_screen_index = 0

    def start_game(self):
        if self._current_screen_index != 0:
            raise RuntimeError("Wrong screen")

        self._equipment = Equipment("")
        self._arena = Arena()
        self._player = None
        self._enemy = None

    def select_player(self, name: str, class_name: str, armor_name: str, weapon_name: str):

        if self._current_screen_index != 1:
            raise RuntimeError("Wrong screen")

        if class_name not in unit_classes:
            raise RuntimeError("Wrong class_name")

        player: interfaces.PlayerUnit = interfaces.PlayerUnit(
            name=name,
            unit_class=unit_classes[class_name]
        )

        if player is None or self._equipment is None:
            raise RuntimeError("player not created")

        armor = self._equipment.get_armor(armor_name)
        weapon = self._equipment.get_weapon(weapon_name)

        if armor is None or weapon is None:
            raise RuntimeError("wrong armor or weapon")

        player.equip_armor(armor)
        player.equip_weapon(weapon)
        self._player = player

    def select_enemy(self, name: str, class_name: str, armor_name: str, weapon_name: str):

        if self._current_screen_index != 2:
            raise RuntimeError("Wrong screen")

        if class_name not in unit_classes:
            raise RuntimeError("Wrong class_name")

        enemy: interfaces.EnemyUnit = interfaces.EnemyUnit(
            name=name,
            unit_class=unit_classes[class_name]
        )

        if enemy is None or self._equipment is None:
            raise RuntimeError("player not created")

        armor = self._equipment.get_armor(armor_name)
        weapon = self._equipment.get_weapon(weapon_name)

        if armor is None or weapon is None:
            raise RuntimeError("wrong armor or weapon")

        enemy.equip_armor(armor)
        enemy.equip_weapon(weapon)
        self._enemy = enemy

        self._arena.start_game(self._player, self._enemy)

    def _end_game(self):
        self._fight_result = self._arena.battle_result if self._arena else ""
        self._arena = None

    def fight(self, action: str):
        if self._current_screen_index != 3 or self._arena is None:
            raise RuntimeError("Wrong screen")

        if action == "hit":
            self._arena.make_a_player_hit()
        elif action == "skill":
            self._arena.use_player_skill()
        elif action == "skip":
            self._arena.skip_turn()
        else:
            raise RuntimeError("Wrong action")

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
