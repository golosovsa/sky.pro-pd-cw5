"""
    Abstract class Arena
"""

from abc import ABC, abstractmethod

from .unit import Unit


class Arena(ABC):

    _player: Unit = NotImplemented
    _enemy: Unit = NotImplemented

    @abstractmethod
    def start_game(self, player, enemy):
        pass

    @abstractmethod
    def make_next_turn(self):
        pass

    @abstractmethod
    def _end_game(self):
        pass

    @abstractmethod
    def make_a_player_hit(self):
        pass

    @abstractmethod
    def use_player_skill(self):
        pass
