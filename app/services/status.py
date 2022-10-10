"""
    Service abstraction level
    Status service class
"""

from typing import List

from .base import BaseService
from app.dao import PlayerDAO


class StatusService(BaseService[PlayerDAO]):
    _updatable_fields: List[str] = []
