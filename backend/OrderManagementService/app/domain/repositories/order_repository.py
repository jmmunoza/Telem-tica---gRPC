import abc

from app.domain.entities.product import Product
from app.domain.entities.order import Order

class OrderRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, order: Order) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, order_id: int) -> Order:
        raise NotImplementedError
    
    @abc.abstractmethod
    def update(self, order: Order) -> None:
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete(self, order: Order) -> None:
        raise NotImplementedError
