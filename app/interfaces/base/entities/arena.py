"""
    Base Arena class implementation
"""

from typing import Optional

from app.interfaces import abstract
from app.interfaces.base import Unit


class Arena(abstract.Arena):

    def __init__(self):
        self._player: Unit | None = None
        self._enemy: Unit | None = None
        self._is_game_running: bool = False
        self._battle_result: str = ""
        self._methods = {
            "hit": "hit",
            "skill": "skill"
        }

    def start_game(self, player: Unit, enemy: Unit):
        self._player = player
        self._enemy = enemy

    def _make_a_turn(self, attacker: Unit, defender: Unit, method, message: str):
        attacker.hit(defender)
        if defender.is_alive:
            return
        self._battle_result = message.format(defender.name)
        self._end_game()

    def make_next_turn(self):
        self._make_a_hit(self._enemy, self._player, "Игрок {} был убит")

    def make_a_player_hit(self):
        self._make_a_hit(self._enemy, self._player, "Игрок {} был убит")

        self._player.hit(self._enemy)
        if self._enemy.is_alive:
            return
        self._battle_result = f"Враг {self._player.name} был убит"
        self._end_game()

    def use_player_skill(self):
        pass

    def _end_game(self):
        return NotImplementedError()
