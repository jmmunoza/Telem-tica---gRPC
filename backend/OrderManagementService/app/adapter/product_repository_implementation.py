from typing import List

from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository

# en app -> sudo python3 -m grpc_tools.protoc -I ../resources/protobufs  --python_out=grpc_generated/inventoryservicegrpc/  --pyi_out=grpc_generated/inventoryservicegrpc/ --grpc_python_out=grpc_generated/inventoryservicegrpc/ ../resources/protobufs/inventoryservice.proto

class ProductRepositoryImplementation(ProductRepository):
    def __init__(self):
        self._products = []

    def add(self, product: Product) -> None:
        self._products.append(product)

    def getAll(self) -> List[Product]:
        return self._products

    def get(self, product_id: int) -> Product:
        return Product(123, 'pRODUCTO PRUBA', 25500) # CAMBIAR
    
    def update(self, product: Product) -> None:
        print(product, "UPDATEEEEEEE")
    
    def delete(self, product: Product) -> None:
        print(product, "DELETEEEEEEEEEE")