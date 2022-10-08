"""
    BattleLog model
"""

from dataclasses import dataclass, field
from typing import List

from app.setup.db.models import BaseWithID


@dataclass
class BattleLog(BaseWithID):
    log: List[str] = field(default_factory=list)
