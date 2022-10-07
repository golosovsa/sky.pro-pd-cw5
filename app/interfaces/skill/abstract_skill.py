"""
    Abstract class Skill
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..unit import BaseUnit


class AbstractSkill(ABC):

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
    def skill_effect(self, user: "BaseUnit", target: "BaseUnit") -> str:
        pass

    @abstractmethod
    def _is_stamina_enough(self, user: "BaseUnit") -> bool:
        pass

    @abstractmethod
    def use(self, user: "BaseUnit", target: "BaseUnit") -> str:
        pass
