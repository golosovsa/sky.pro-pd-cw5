"""
    Service abstraction level
    BattleLog service class
"""
from typing import List, Optional

from .base import BaseService
from app.dao import BattleLogDAO
from ..dao.models import BattleLog as BattleLogModel


class BattleLogService(BaseService[BattleLogDAO]):
    _updatable_fields: List[str] = []

    def __init__(self, dao: BattleLogDAO):
        super().__init__(dao)
        self._dao: BattleLogDAO = dao

    def get_item(self, pk: int) -> Optional[BattleLogModel]:
        return self._dao.get_by_id(pk)
