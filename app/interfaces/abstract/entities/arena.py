"""
    Abstract class Arena
"""

from abc import ABC, abstractmethod

from ..patterns.singleton_meta import SingletonMeta
from .unit import Unit


class Arena(SingletonMeta, ABC):

    _player: Unit = NotImplemented
    _enemy: Unit = NotImplemented
    _is_game_running: bool = NotImplemented

    @abstractmethod
    def start_game(self, player: Unit, enemy: Unit):
        pass

    @abstractmethod
    def _check_players_hp(self):
        pass

    @abstractmethod
    def _regenerate_stamina(self):
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
