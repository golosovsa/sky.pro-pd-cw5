"""
    Class BattleLog Singleton implementation
"""

from typing import TYPE_CHECKING

from .battle_log import BaseBattleLog
from .singleton_meta import BaseSingletonMeta as SingletonMeta

if TYPE_CHECKING:
    ABCSingletonBattleLogMeta = type
else:
    class ABCSingletonBattleLogMeta(SingletonMeta, type(BaseBattleLog)):
        pass


class BattleLog(BaseBattleLog, metaclass=ABCSingletonBattleLogMeta):

    def __init__(self):
        super().__init__()
