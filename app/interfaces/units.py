"""
    Class Skills implementation
"""
from random import randint

from app.interfaces import base
from .abstract.entities.unit import TUnit
from .battle_log import BattleLog


class PlayerUnit(base.Unit):

    def _log(self, message: str):
        BattleLog()(message)


class EnemyUnit(base.Unit):

    def _log(self, message: str):
        BattleLog()(message)

    def hit(self, target: TUnit):
        if not randint(0, 10):
            self.use_skill(target)
            return

        super(EnemyUnit, self).hit(target)
