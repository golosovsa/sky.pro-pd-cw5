"""
    Test base BattleLog
"""

from app.interfaces.battle_log import BaseBattleLog as BattleLog


class TestBattleLog:

    def test_constructor(self):
        log = BattleLog()
        assert log._log == []

    def test_call(self):
        log = BattleLog()
        log("test_string_1")
        log("test_string_2")
        log("test_string_3")

        assert len(log._log) == 3

    def test_flush(self):
        log = BattleLog()
        log("test_string_1")
        log("test_string_2")
        log("test_string_3")

        logs = log.flush()

        assert len(logs) == 3
        assert "test_string_1" in logs
        assert "test_string_2" in logs
        assert "test_string_3" in logs

        assert len(log._log) == 0
