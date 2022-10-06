"""
    Base Unit class implementation
"""
from typing import Union

from app.interfaces import abstract
from app.interfaces.abstract.entities.unit import TUnit
from .weapon import Weapon
from .armor import Armor
from .unit_class import UnitClass


class Unit(abstract.Unit):

    _STAMINA_PER_TURN: float = 1.0
    _EPSILON = 0.1

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

        defence_points = round(self._armor.defence * self._unit_class.armor, 1)
        self._log(f"{self.name} защищается {defence_points} пунктами защиты")
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

        damage_points = round(self._weapon.damage * self._unit_class.attack, 1)
        self._log(f"{self.name} атакует, его атака равна {damage_points} пунктов")
        return damage_points

    def _count_damage(self, target: TUnit) -> float:
        damage = round(self.damage - target.defence, 1)
        damage = damage if damage > self._EPSILON else 0
        self._log(f"Урон с учетом защиты составит {damage} единиц")
        return damage

    def _regenerate_stamina(self):
        stamina_regeneration = self._STAMINA_PER_TURN * self._unit_class.stamina
        self._stamina += stamina_regeneration
        self._log(f"{self.name} восстанавливает {stamina_regeneration} выносливости до {self._stamina} единиц")

    def get_damage(self, damage: float):
        self._regenerate_stamina()
        if damage < self._EPSILON:
            self._log(f"{self.name} не получает урона")
            return 0
        self._hp -= damage
        if self._armor:
            self._log(f"{self.name} тратит {damage} очков выносливости на защиту")
            self._stamina -= self._armor.stamina_per_turn
        self._log(f"{self.name} получает {damage} очков повреждения, его здоровье уменьшается до {self._hp} очков")

    def hit(self, target: TUnit):
        self._regenerate_stamina()
        damage = self._count_damage(target)
        target.get_damage(damage)

    def use_skill(self, target: TUnit):
        if self._is_skill_used:
            self._log(f"{self.name} попытался использовать "
                      f"{self._unit_class.skill.name}, "
                      f"но это можно сделать только один раз за бой, "
                      f"поэтому будет нанесен обычный удар")
            self.hit(target)
            return
        self._regenerate_stamina()
        user: Union[TUnit, Unit] = self
        message = self._unit_class.skill.use(user, target)
        self._log(message)

    def skip_turn(self, target: TUnit):
        self._regenerate_stamina()
        self._log(f"{self.name} пропускает ход")
