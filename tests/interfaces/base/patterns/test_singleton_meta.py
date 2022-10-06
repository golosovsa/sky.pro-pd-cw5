"""
    Test SingletonMeta base implementation
"""

from app.interfaces.base import SingletonMeta


class SingletonClass(metaclass=SingletonMeta):
    pass


class AnotherSingletonClass(metaclass=SingletonMeta):
    pass


class TestSingleton:

    def test_singleton(self):
        single_1 = SingletonClass()
        single_2 = SingletonClass()
        another_single_1 = AnotherSingletonClass()
        another_single_2 = AnotherSingletonClass()
        assert single_1 is not None
        assert single_1 is single_2
        assert id(single_1) == id(single_2)
        assert id(another_single_1) == id(another_single_2) != id(None)
        assert id(single_1) != id(another_single_1)
