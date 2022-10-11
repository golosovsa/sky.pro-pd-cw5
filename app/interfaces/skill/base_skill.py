"""
    Base Skill class implementation
"""

from typing import Optional, TYPE_CHECKING

from .abstract_skill import AbstractSkill

if TYPE_CHECKING:
    from ..unit import BaseUnit


class BaseSkill(AbstractSkill):

    _name: str = NotImplemented
    _stamina: float = NotImplemented
    _damage: float = NotImplemented

    def __init__(self,
                 name: Optional[str] = None,
                 stamina: Optional[float] = None,
                 damage: Optional[float] = None):

        if name:
            setattr(self, "_name", name)
        if stamina is not None:
            setattr(self, "_stamina", stamina)
        if damage is not None:
            setattr(self, "_damage", damage)

    @property
    def name(self) -> str:
        return self._name

    @property
    def stamina(self) -> float:
        return self._stamina

    @property
    def damage(self) -> float:
        return self._damage

    def skill_effect(self, user: "BaseUnit", target: "BaseUnit") -> str:
        user.stamina_points -= self._stamina
        defence = target.defence
        damage = target.get_damage(self._damage - defence)
        return f"{user.name} успешно использовал " \
               f"{self.name} и нанес " \
               f"{damage:.2f} урона сопернику " \
               f"{target.name}"

    def _is_stamina_enough(self, user: "BaseUnit") -> bool:
        return user.stamina_points >= self._stamina

    def use(self, user: "BaseUnit", target: "BaseUnit") -> str:
        if not self._is_stamina_enough(user):
            return f"{user.name} попытался использовать " \
                   f"{self.name} но у него не хватило выносливости."

        return self.skill_effect(user, target)
