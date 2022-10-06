"""
    Class Arena implementation
"""
from typing import TYPE_CHECKING

from app.interfaces import base
from .battle_log import BattleLog

if TYPE_CHECKING:
    ABCSingletonArenaMeta = type
else:
    class ABCSingletonArenaMeta(base.SingletonMeta, type(base.Arena)):
        pass


class Arena(base.Arena, metaclass=ABCSingletonArenaMeta):

    def __init__(self):
        super().__init__()

    def _end_game(self):
        BattleLog()(message=self._battle_result)
        self._instances = {}
