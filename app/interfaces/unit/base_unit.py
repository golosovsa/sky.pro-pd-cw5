"""
    Base Unit class implementation
"""

from typing import Optional

from .abstract_unit import AbstractUnit
from ..weapon import BaseWeapon as Weapon
from ..armor import BaseArmor as Armor
from ..unit_class import BaseUnitClass as UnitClass


class BaseUnit(AbstractUnit):

    _STAMINA_PER_TURN: float = 1.0
    _EPSILON = 0.1
    _FRACTIONAL = 2

    def __init__(self, name: str, unit_class: UnitClass):
        self._name: str = name
        self._unit_class: UnitClass = unit_class
        self._hp: float = unit_class.max_health
        self._stamina: float = unit_class.max_stamina
        self._weapon: Weapon | None = None
        self._armor: Armor | None = None
        self._is_skill_used: bool = False

    @property
    def name(self):
        return self._name

    @property
    def health_points(self):
        return self._hp

    @property
    def unit_class(self) -> str:
        return self._unit_class.name

    @property
    def weapon(self) -> Optional[str]:
        if self._weapon:
            return self._weapon.name
        return None

    @property
    def armor(self) -> Optional[str]:
        if self._armor:
            return self._armor.name
        return None

    @property
    def is_alive(self):
        return self._hp > self._EPSILON

    @property
    def stamina_points(self):
        return self._stamina

    @stamina_points.setter
    def stamina_points(self, value: float):
        self._stamina = value

    def equip_weapon(self, weapon: Weapon):
        self._weapon = weapon

    def equip_armor(self, armor: Armor):
        self._armor = armor

    def _log(self, message: str):
        raise NotImplementedError()

    @property
    def defence(self) -> float:
        if self._armor is None:
            self._log(f"{self.name} забыл одеть броню, его защита 0")
            return 0

        if self._stamina < self._armor.stamina_per_turn:
            self._log(f"{self.name} Не имеет достаточного количества выносливости для защиты")
            return 0

        defence_points = round(self._armor.defence * self._unit_class.armor, self._FRACTIONAL)
        self._log(f"{self.name} защищается {defence_points:.2f} пунктами защиты")
        return defence_points

    @property
    def damage(self) -> float:
        if self._weapon is None:
            self._log(f"{self.name} забыл взять оружие, его атака 0")
            self.skip_turn(self)
            return 0

        if self._stamina < self._weapon.stamina_per_hit:
            self._log(f"{self.name} Не имеет достаточного количества выносливости для атаки")
            return 0

        damage_points = round(self._weapon.damage * self._unit_class.attack, self._FRACTIONAL)
        self._log(f"{self.name} атакует, его атака равна {damage_points:.2f} пунктов")
        return damage_points

    def _count_damage(self, target: "BaseUnit") -> float:
        damage = round(self.damage - target.defence, self._FRACTIONAL)
        damage = damage if damage > self._EPSILON else 0
        self._log(f"Урон с учетом защиты составит {damage:.2f} единиц")
        return damage

    def _regenerate_stamina(self):
        stamina_regeneration = round(self._STAMINA_PER_TURN * self._unit_class.stamina, self._FRACTIONAL)
        self._stamina += stamina_regeneration
        self._log(f"{self.name} восстанавливает {stamina_regeneration:.2f} выносливости до {self._stamina:.2f} единиц")

    def get_damage(self, damage: float):
        self._regenerate_stamina()
        if self._armor:
            self._stamina -= self._armor.stamina_per_turn
            self._log(f"{self.name} тратит "
                      f"{self._armor.stamina_per_turn:.2f} очков выносливости на защиту, его выносливость становится "
                      f"{self._stamina:.2f} очков")
        if damage < self._EPSILON:
            self._log(f"{self.name} не получает урона")
            return 0
        self._hp -= damage
        self._log(f"{self.name} получает "
                  f"{damage:.2f} очков повреждения, его здоровье уменьшается до "
                  f"{self._hp:.2f} очков")
        return damage

    def hit(self, target: "BaseUnit"):
        damage = self._count_damage(target)
        if self._weapon is None:
            self.skip_turn(target)
            return
        if damage < self._EPSILON and self._stamina < self._weapon.stamina_per_hit:
            self.skip_turn(target)
            return

        self._regenerate_stamina()
        self._stamina -= self._weapon.stamina_per_hit
        self._log(f"{self.name} тратит "
                  f"{self._weapon.stamina_per_hit:.2f} очков выносливости на атаку, "
                  f"его выносливость становится {self._stamina:.2f} очков")
        target.get_damage(damage)

    def use_skill(self, target: "BaseUnit"):
        if self._is_skill_used:
            self._log(f"{self.name} попытался использовать "
                      f"{self._unit_class.skill.name}, "
                      f"но это можно сделать только один раз за бой, "
                      f"поэтому будет нанесен обычный удар")
            self.hit(target)
            return
        self._is_skill_used = True
        self._regenerate_stamina()
        user: BaseUnit = self
        self._log(f"{self.name} использует навык")
        message = self._unit_class.skill.use(user, target)
        self._log(message)

    def skip_turn(self, target: "BaseUnit"):
        self._regenerate_stamina()
        self._log(f"{self.name} пропускает ход")
        self._log(f"{target.name} не получает урона и не восстанавливает выносливость")
