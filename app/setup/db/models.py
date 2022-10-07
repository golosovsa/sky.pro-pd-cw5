"""
    base model
"""

from dataclasses import dataclass


@dataclass
class Base:
    pass


@dataclass
class BaseWithID:
    id: int
