"""
    Status model
"""

from dataclasses import dataclass
from app.setup.db.models import BaseWithID


@dataclass
class Status(BaseWithID):
    user_pk: int
    current_page: str
    server_status: str = "online"
