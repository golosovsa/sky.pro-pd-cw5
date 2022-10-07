"""
    Class BattleLog implementation
"""

from typing import List

from .abstract_battle_log import AbstractBattleLog


class BaseBattleLog(AbstractBattleLog):

    def __init__(self):
        self._log: List[str] = []

    def __call__(self, message: str):
        self._log.append(message)

    def flush(self) -> List[str]:
        log, self._log = self._log, []
        return log
