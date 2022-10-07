"""
    Testing class Arena Singleton
"""

from app.interfaces import Arena


class TestArenaSingleton:

    def test_singleton(self):
        arena_1 = Arena()
        arena_2 = Arena()
        assert id(arena_1) == id(arena_2)
