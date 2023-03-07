import abc
from typing import List

from app.domain.entities.product import Product

class ProductRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, product: Product) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def getAll(self) -> List[Product]:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, product_id: int) -> Product:
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete(self, product: Product) -> bool:
        raise NotImplementedError
