from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2_grpc
from app.adapter.product_repository_implementation import ProductRepositoryImplementation


class InventoryService(inventoryservice_pb2_grpc.InventoryServiceServicer):
    def __init__(self) -> None:
        super().__init__()
        self._product_repository = ProductRepositoryImplementation()

    def getAll(self, request, context):
        
        print(str(request), "getAll")
        return self._product_repository.getAll()

    def add(self, request, context):
        print(str(request), "add")
        self._product_repository.add()

    def get(self, request, context):
        print(request, "get")
        return inventoryservice_pb2.Product(produtct_id=1, price=123, name="MANOLO")
        return self._product_repository.get()

    def update(self, request, context):
        print(request, "update")
        self._product_repository.update()

    def delete(self, request, context):
        print(request, "delete")
        self._product_repository.delete()

    """
   	def AddProduct(self, request, context):
      	print("Request is received: " + str(request))
      	return Service_pb2.TransactionResponse(status_code=1)
    """
