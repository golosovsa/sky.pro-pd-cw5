"""
    Service abstraction level
    Enemy service class
"""

from .base import BaseService
from app.dao import EnemyDAO


class EnemyService(BaseService[EnemyDAO]):
    _updatable_fields = ["unit_class", "weapon", "armor", ]
