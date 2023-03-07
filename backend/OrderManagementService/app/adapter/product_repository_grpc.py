from typing import List

from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository

import grpc, os
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2, inventoryservice_pb2_grpc
from google.protobuf.json_format import MessageToDict

INVENTORY_SERVICE_ADDRESS = os.getenv('INVENTORY_SERVICE_ADDRESS')

# en app -> sudo python3 -m grpc_tools.protoc -I ../resources/protobufs  --python_out=grpc_generated/inventoryservicegrpc/  --pyi_out=grpc_generated/inventoryservicegrpc/ --grpc_python_out=grpc_generated/inventoryservicegrpc/ ../resources/protobufs/inventoryservice.proto

class ProductRepositoryGrpc(ProductRepository):
    def __init__(self):
        self._products = []

    def add(self, product: Product) -> bool:
        self._products.append(product)

    def getAll(self) -> List[Product]:
        return self._products

    def get(self, product_id: int) -> Product:
        return Product(123, 'pRODUCTO PRUBA', 25500) # CAMBIAR

    def delete(self, product_id: int) -> bool:
        with grpc.insecure_channel(INVENTORY_SERVICE_ADDRESS) as channel:
            stub     = inventoryservice_pb2_grpc.InventoryServiceStub(channel)
            response = stub.delete(inventoryservice_pb2.DeleteProductRequest(produtct_id=product_id))
                    
        response_dict = MessageToDict(response)
        
        return response_dict['is_successful']