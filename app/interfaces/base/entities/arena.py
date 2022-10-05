"""
    Base Arena class implementation
"""
from typing import Callable

from app.interfaces import abstract
from app.interfaces.base import Unit


class Arena(abstract.Arena):

    def __init__(self):
        self._player: Unit | None = None
        self._enemy: Unit | None = None
        self._is_game_running: bool = False
        self._battle_result: str = ""

    @property
    def is_game_run(self):
        return self._battle_result == ""

    def start_game(self, player: Unit, enemy: Unit):
        self._player = player
        self._enemy = enemy

    def _make_a_turn(self, attacker: Unit, defender: Unit, message: str, method: Callable):
        method(self=attacker, target=defender)
        if defender.is_alive:
            return
        self._battle_result = message.format(defender.name)
        self._end_game()

    def make_next_turn(self):
        self._make_a_turn(self._enemy, self._player, "Игрок {} был убит", Unit.hit)

    def make_a_player_hit(self):
        self._make_a_turn(self._enemy, self._player, "Враг {} был убит", Unit.hit)

    def use_player_skill(self):
        self._make_a_turn(self._enemy, self._player, "Враг {} был убит", Unit.use_skill)

    def _end_game(self):
        return NotImplementedError()
