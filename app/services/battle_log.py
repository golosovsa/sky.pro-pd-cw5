"""
    Service abstraction level
    BattleLog service class
"""

from typing import List

from .base import BaseService
from app.dao import BattleLogDAO


class BattleLogService(BaseService[BattleLogDAO]):
    _updatable_fields: List[str] = []
