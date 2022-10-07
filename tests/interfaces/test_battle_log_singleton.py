"""
    Testing class BattleLog Singleton
"""

from app.interfaces import BattleLog


class TestBattleLogSingleton:

    def test_singleton(self):
        log_1 = BattleLog()
        log_2 = BattleLog()
        assert id(log_1) == id(log_2)
