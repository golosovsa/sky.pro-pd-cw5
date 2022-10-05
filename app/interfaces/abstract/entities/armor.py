"""
    Abstract class Armor
"""

from abc import ABC
from typing import TypeVar

TArmor = TypeVar("TArmor", bound="Armor")


class Armor(ABC):
    id: int = NotImplemented
    name: str = NotImplemented
    defence: float = NotImplemented
    stamina_per_turn: float = NotImplemented
