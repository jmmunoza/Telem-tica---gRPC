from concurrent import futures
from app.services.inventory_service import InventoryService
import grpc, os, dotenv
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2_grpc

dotenv.load_dotenv()
INVENTORY_SERVICE_ADDRESS = os.getenv('INVENTORY_SERVICE_ADDRESS')

def serve():
    # Creating the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Adding Inventory Service to the server
    inventoryservice_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryService(), server)

    # Starting the server
    print("Server is running...")
    server.add_insecure_port(INVENTORY_SERVICE_ADDRESS)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
