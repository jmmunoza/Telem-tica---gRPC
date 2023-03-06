from app.domain.entities.order import Order
from app.domain.repositories.order_repository import OrderRepository

# en app -> sudo python3 -m grpc_tools.protoc -I ../resources/protobufs  --python_out=grpc_generated/ordermanagementservicegrpc/  --pyi_out=grpc_generated/ordermanagementservicegrpc/ --grpc_python_out=grpc_generated/ordermanagementservicegrpc/ ../resources/protobufs/ordermanagementservice.proto

class OrderRepositoryImplementation(OrderRepository):
    def __init__(self):
        self._orders = []

    def add(self, order: Order) -> None:
        self._orders.append(order)

    def get(self, order_id: int) -> Order:
        return Order(10, 15, 25500) # CAMBIAR
    
    def update(self, order: Order) -> None:
        print(order, "UPDATEEEEEEE")
    
    def delete(self, order: Order) -> None:
        print(order, "DELETEEEEEEEEEE")