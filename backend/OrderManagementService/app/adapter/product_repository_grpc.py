from typing import List

from app.domain.entities.product import Product
from app.domain.repositories.product_repository import ProductRepository

import grpc, os, dotenv
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2, inventoryservice_pb2_grpc
from google.protobuf.json_format import MessageToDict

from app.parser.product_parser import dict_to_product

dotenv.load_dotenv()
INVENTORY_SERVICE_ADDRESS = os.getenv('INVENTORY_SERVICE_ADDRESS')

# en app -> sudo python3 -m grpc_tools.protoc -I ../resources/protobufs  --python_out=grpc_generated/inventoryservicegrpc/  --pyi_out=grpc_generated/inventoryservicegrpc/ --grpc_python_out=grpc_generated/inventoryservicegrpc/ ../resources/protobufs/inventoryservice.proto

class ProductRepositoryGrpc(ProductRepository):
    def __init__(self):
        self._products = []

    def add(self, name: str, price: float, stock: int) -> Product:
        pass

    def getAll(self) -> List[Product]:
        pass
    
    def update(self, product: Product) -> bool:
        pass

    def get(self, product_id: str) -> Product:
        with grpc.insecure_channel(INVENTORY_SERVICE_ADDRESS) as channel:
            stub     = inventoryservice_pb2_grpc.InventoryServiceStub(channel)
            response = stub.get(inventoryservice_pb2.GetProductRequest(product_id=product_id))
                    
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        product = dict_to_product(response_dict)
        
        return product


    def delete(self, product_id: str) -> bool:
        with grpc.insecure_channel(INVENTORY_SERVICE_ADDRESS) as channel:
            stub     = inventoryservice_pb2_grpc.InventoryServiceStub(channel)
            response = stub.delete(inventoryservice_pb2.DeleteProductRequest(product_id=product_id))
                    
        response_dict = MessageToDict(response, preserving_proto_field_name=True )
        return response_dict['is_successful']