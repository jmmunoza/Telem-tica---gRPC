from app.grpc_generated.ordermanagementservicegrpc import ordermanagementservice_pb2, ordermanagementservice_pb2_grpc
from app.adapter.order_respository_implementation import OrderRepositoryImplementation


class OrderManagementService(ordermanagementservice_pb2_grpc.OrderManagementServiceServicer):
    def __init__(self) -> None:
        super().__init__()
        self._order_repository = OrderRepositoryImplementation()

    def add(self, request, context):
        print(request, "add")
        self._order_repository.add()

    def get(self, request, context):
        print(request, "get")
        return ordermanagementservice_pb2.Order(order_id=3, produtct_id=1, amount=2)
        return self._order_repository.get()

    def update(self, request, context):
        print(request, "update")
        self._order_repository.update()

    def delete(self, request, context):
        print(request, "delete")
        self._order_repository.delete()

    """
   	def AddProduct(self, request, context):
      	print("Request is received: " + str(request))
      	return Service_pb2.TransactionResponse(status_code=1)
    """
