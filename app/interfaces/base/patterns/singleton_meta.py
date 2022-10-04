"""
    Base class SingletonMeta
"""
from typing import Dict

from app.interfaces import abstract


class SingletonMeta(type, abstract.SingletonMeta):
    _instances: Dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            return cls._instances[cls]

        instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance
        return instance

    # def __new__(mcs, *args, **kwargs):
    #     if mcs in mcs._instances:
    #         return mcs._instances[mcs]
    #     return super().__new__(mcs, *args, **kwargs)
