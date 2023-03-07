from concurrent import futures
import grpc, os, dotenv

# Import Services
from app.services.order_management_service import OrderManagementService
from app.services.inventory_service import InventoryService

# Import Grpc Services
from app.grpc_generated.ordermanagementservicegrpc import ordermanagementservice_pb2_grpc
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2_grpc, inventoryservice_pb2

dotenv.load_dotenv()
ORDER_MANAGEMENT_SERVICE_ADDRESS = os.getenv('ORDER_MANAGEMENT_SERVICE_ADDRESS')
INVENTORY_SERVICE_ADDRESS        = os.getenv('INVENTORY_SERVICE_ADDRESS')

def serve():
    # Creating the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Adding Order Management Service to the server
    ordermanagementservice_pb2_grpc.add_OrderManagementServiceServicer_to_server(
        OrderManagementService(), server)

    # Adding Inventory Service to the server
    inventoryservice_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryService(), server)

    # Starting the server
    print("Server is running...")
    server.add_insecure_port(ORDER_MANAGEMENT_SERVICE_ADDRESS)
    server.start()
    server.wait_for_termination()

from google.protobuf.json_format import MessageToDict

def run():
    with grpc.insecure_channel(INVENTORY_SERVICE_ADDRESS) as channel:
        stub = inventoryservice_pb2_grpc.InventoryServiceStub(channel)
        response = stub.get(inventoryservice_pb2.ProductRetrieveRequest(produtct_id=4))
        #response = stub.add(inventoryservice_pb2.Product(produtct_id=3, name="Pacaaaaaaa", price=9000))
    print(MessageToDict(response))   
    
    '''
    with grpc.insecure_channel(HOST) as channel:
        stub = inventoryservice_pb2_grpc.InventoryServiceStub(channel)
        response = stub.add(inventoryservice_pb2.Product(produtct_id=3, name="Pedro", price=400), metadata={'product'})

    print(response.message)   
    
    with grpc.insecure_channel(HOST) as channel:
        stub = inventoryservice_pb2_grpc.InventoryServiceStub(channel)
        response = stub.getAll()
    print(response.message)  
    '''
    


if __name__ == "__main__":
    run()
    #serve()
