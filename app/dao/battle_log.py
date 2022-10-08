"""
    DAO abstraction level
    BattleLog DAO
"""
from typing import Type, Optional, List

from .base import BaseDAO
from .models import BattleLog as BattleLogModel
from app.game_container import BattleLog


class BattleLogDAO(BaseDAO[BattleLogModel]):
    __model__: Type[BattleLogModel] = BattleLogModel
    _data: Type[BattleLog] = BattleLog

    def get_by_id(self, pk: int) -> Optional[BattleLogModel]:
        return BattleLogModel(
            id=0,
            log=self._data().flush(),
        )

    def get_all(self, page: Optional[int] = None) -> List[BattleLogModel]:
        return []

    def create(self, model: BattleLogModel):
        return None

    def update(self, model: BattleLogModel):
        return None

    def delete(self, model: BattleLogModel):
        return None
