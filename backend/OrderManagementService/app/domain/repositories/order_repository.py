import abc
from typing import List

from app.domain.entities.order import Order

class OrderRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getAll(self) -> List[Order]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def create(self, product_id: str, amount: float) -> Order:
        raise NotImplementedError

    @abc.abstractmethod
    def cancel(self, order_id: str) -> bool:
        raise NotImplementedError
    
    @abc.abstractmethod
    def complete(self, order_id: str) -> bool:
        raise NotImplementedError
