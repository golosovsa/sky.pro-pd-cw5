"""
    Class Skills implementation
"""
from random import randint

from .unit import BaseUnit
from .battle_log_singleton import BattleLog


class PlayerUnit(BaseUnit):

    def _log(self, message: str):
        BattleLog()(message)


class EnemyUnit(BaseUnit):

    def _log(self, message: str):
        BattleLog()(message)

    def hit(self, target: BaseUnit):
        if not randint(0, 10):
            self.use_skill(target)
            return

        super(EnemyUnit, self).hit(target)
