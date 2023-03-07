from typing import List

from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository

from uuid import uuid4

# en app -> sudo python3 -m grpc_tools.protoc -I ../resources/protobufs  --python_out=grpc_generated/inventoryservicegrpc/  --pyi_out=grpc_generated/inventoryservicegrpc/ --grpc_python_out=grpc_generated/inventoryservicegrpc/ ../resources/protobufs/inventoryservice.proto

class ProductRepositoryImplementation(ProductRepository):
    def __init__(self):
        self._products = []

    def add(self, name: str, price: float, stock: int) -> Product:
        product_id  = str(uuid4())
        product     = Product(product_id, name, price, stock)
        
        self._products.append(product)
        return product

    def getAll(self) -> List[Product]:
        return self._products

    def get(self, product_id: str) -> Product:
        for product in self._products:
            if product.getId() == product_id:
                return product
            
        return None
    
    def delete(self, product_id: str) -> bool:
        for product_to_delete in self._products:
            if product_to_delete.getId() == product_id:
                self._products.remove(product_to_delete)
                return True
        
        return False