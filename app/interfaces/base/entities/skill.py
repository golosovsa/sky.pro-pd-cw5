"""
    Base Skill class implementation
"""

from typing import Optional

from app.interfaces import abstract
from app.interfaces.abstract.entities.skill import TUnit


class Skill(abstract.Skill):

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

    def skill_effect(self, user: TUnit, target: TUnit) -> str:
        user.stamina_points -= self._stamina
        defence = target.defence
        damage = target.get_damage(self._damage - defence)
        return f"{user.name} успешно использовал " \
               f"{self.name} и нанес " \
               f"{damage} урона сопернику " \
               f"{target.name}"

    def _is_stamina_enough(self, user: TUnit) -> bool:
        return user.stamina_points >= self._stamina

    def use(self, user: TUnit, target: TUnit) -> str:
        if not self._is_stamina_enough(user):
            return f"{user.name} попытался использовать " \
                   f"{self.name} но у него не хватило выносливости."

        return self.skill_effect(user, target)
