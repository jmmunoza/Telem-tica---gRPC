import abc
from typing import List

from app.domain.entities.product import Product

class ProductRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, name: str, price: float, stock: int) -> Product:
        raise NotImplementedError

    @abc.abstractmethod
    def getAll(self) -> List[Product]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, product_id: str) -> Product:
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete(self, product_id: str) -> bool:
        raise NotImplementedError
