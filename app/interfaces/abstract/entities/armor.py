"""
    Abstract class Armor
"""

from abc import ABC


class Armor(ABC):
    id: int = NotImplemented
    name: str = NotImplemented
    defence: float = NotImplemented
    stamina_per_turn: float = NotImplemented
