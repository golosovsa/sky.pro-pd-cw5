"""
    Abstract class Arena
"""

from abc import ABC, abstractmethod

from ..unit import BaseUnit as Unit


class AbstractArena(ABC):

    @abstractmethod
    def start_game(self, player: Unit, enemy: Unit):
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

    @abstractmethod
    def skip_turn(self):
        pass
