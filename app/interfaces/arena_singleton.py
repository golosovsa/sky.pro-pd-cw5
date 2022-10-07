"""
    Class Arena Singleton implementation
"""
from typing import TYPE_CHECKING

from .arena import BaseArena
from .singleton_meta import BaseSingletonMeta as SingletonMeta
from .battle_log_singleton import BattleLog

if TYPE_CHECKING:
    ABCSingletonArenaMeta = type
else:
    class ABCSingletonArenaMeta(SingletonMeta, type(BaseArena)):
        pass


class Arena(BaseArena, metaclass=ABCSingletonArenaMeta):

    def __init__(self):
        super().__init__()

    def _end_game(self):
        BattleLog()(self._battle_result)
        self._instances = {}
