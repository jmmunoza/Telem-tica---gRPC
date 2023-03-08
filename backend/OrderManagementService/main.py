from concurrent import futures
import grpc, os, dotenv

# Import Services
from app.services.order_management_service import OrderManagementService

# Import Grpc Services
from app.grpc_generated.ordermanagementservicegrpc import ordermanagementservice_pb2_grpc
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2_grpc

dotenv.load_dotenv()
ORDER_MANAGEMENT_SERVICE_ADDRESS = os.getenv('ORDER_MANAGEMENT_SERVICE_ADDRESS')

def serve():
    # Creating the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Adding Order Management Service to the server
    ordermanagementservice_pb2_grpc.add_OrderManagementServiceServicer_to_server(
        OrderManagementService(), server)

    # Starting the server
    print("Server is running...")
    server.add_insecure_port(ORDER_MANAGEMENT_SERVICE_ADDRESS)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()