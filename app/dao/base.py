"""
    DAO abstraction level
    Base DAO
"""

from typing import TypeVar, Generic, Optional, List, Type

T = TypeVar('T')


class BaseDAO(Generic[T]):
    __model__: Type[T]

    def get_by_id(self, pk: int) -> Optional[T]:
        raise NotImplementedError()

    def get_all(self) -> List[T]:
        raise NotImplementedError()

    def create(self, model: T):
        raise NotImplementedError()

    def update(self, model: T):
        raise NotImplementedError()

    def delete(self, model: T):
        raise NotImplementedError()
