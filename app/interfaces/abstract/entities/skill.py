"""
    Abstract class Skill
"""

from abc import ABC, abstractmethod
from typing import TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .unit import Unit
TUnit = TypeVar("TUnit", bound="Unit")


class Skill(ABC):
    _name: str = NotImplemented
    _stamina: float = NotImplemented
    _damage: float = NotImplemented

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def stamina(self) -> float:
        pass

    @property
    @abstractmethod
    def damage(self) -> float:
        pass

    @abstractmethod
    def skill_effect(self, user: TUnit, target: TUnit) -> str:
        pass

    @abstractmethod
    def _is_stamina_enough(self, user: TUnit) -> bool:
        pass

    @abstractmethod
    def use(self, user: TUnit, target: TUnit) -> str:
        pass
