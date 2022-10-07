"""
    Base class SingletonMeta
"""
from typing import Dict


class BaseSingletonMeta(type):
    _instances: Dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            return cls._instances[cls]

        instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance
        return instance
