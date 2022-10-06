"""
    Test base BattleLog
"""

from app.interfaces import base


class TestBattleLog:

    def test_constructor(self):
        log = base.BattleLog()
        assert log._log == []

    def test_call(self):
        log = base.BattleLog()
        log("test_string_1")
        log("test_string_2")
        log("test_string_3")

        assert len(log._log) == 3

    def test_flush(self):
        log = base.BattleLog()
        log("test_string_1")
        log("test_string_2")
        log("test_string_3")

        logs = log.flush()

        assert len(logs) == 3
        assert "test_string_1" in logs
        assert "test_string_2" in logs
        assert "test_string_3" in logs

        assert len(log._log) == 0
