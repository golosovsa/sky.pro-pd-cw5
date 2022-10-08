"""
    Service abstraction level
    Player service class
"""

from .base import BaseService
from app.dao import PlayerDAO


class PlayerService(BaseService[PlayerDAO]):
    _updatable_fields = ["unit_class", "weapon", "armor", ]
