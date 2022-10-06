"""
    Class BattleLog implementation
"""

from typing import TYPE_CHECKING

from app.interfaces import base

if TYPE_CHECKING:
    ABCSingletonBattleLogMeta = type
else:
    class ABCSingletonBattleLogMeta(base.SingletonMeta, type(base.BattleLog)):
        pass


class BattleLog(base.BattleLog, metaclass=ABCSingletonBattleLogMeta):

    def __init__(self):
        super(BattleLog, self).__init__()
