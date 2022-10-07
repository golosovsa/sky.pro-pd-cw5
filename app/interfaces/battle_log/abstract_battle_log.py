"""
    Abstract class BattleLog
"""

from abc import ABC, abstractmethod
from typing import List


class AbstractBattleLog(ABC):

    @abstractmethod
    def __call__(self, message: str):
        pass

    @abstractmethod
    def flush(self) -> List[str]:
        pass
