from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository
from typing import List
from uuid import uuid4
from app.adapter.product_repository_grpc import ProductRepositoryGrpc

# en app -> sudo python3 -m grpc_tools.protoc -I ../resources/protobufs  --python_out=grpc_generated/ordermanagementservicegrpc/  --pyi_out=grpc_generated/ordermanagementservicegrpc/ --grpc_python_out=grpc_generated/ordermanagementservicegrpc/ ../resources/protobufs/ordermanagementservice.proto

class OrderRepositoryImplementation(OrderRepository):
    def __init__(self):
        self._orders = []
        self._inventory_repository = ProductRepositoryGrpc()

    def getAll(self) -> List[Order]:
        return self._orders
    
    def create(self, product_id: str, amount: float) -> Order:
        order_id  = str(uuid4())
        new_order = Order(order_id, product_id, amount)
        
        self._orders.append(new_order)
        
        return new_order

    def cancel(self, order_id: str) -> bool:
        for order in self._orders:
            if order_id == order.getId():
                self._orders.remove(order)
                return True
            
        return False

    def complete(self, order_id: str) -> bool:
        for order in self._orders:
            if order_id == order.getId():
                # Llamar a inventory con grpc
                
                # Metodo para restar de stock
                is_successful = self._inventory_repository.delete(order.getProductId())

                if is_successful:
                    self._orders.remove(order)
                
                return is_successful
            
        return False