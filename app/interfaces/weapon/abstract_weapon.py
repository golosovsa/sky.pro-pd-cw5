"""
    Abstract class Weapon
"""

from abc import ABC, abstractmethod


class AbstractWeapon(ABC):

    @property
    @abstractmethod
    def damage(self):
        pass
