"""
    Abstract class SingletonMeta
"""

from abc import ABC, abstractmethod
from typing import Dict, Type


class SingletonMeta(ABC):
    _instances: Dict[Type[object], object] = NotImplemented

    @classmethod
    @abstractmethod
    def __call__(cls, *args, **kwargs):
        pass
