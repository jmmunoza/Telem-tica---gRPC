from app.grpc_generated.ordermanagementservicegrpc import ordermanagementservice_pb2, ordermanagementservice_pb2_grpc
from app.adapter.order_respository_implementation import OrderRepositoryImplementation
from app.parser.order_parser import order_list_to_grpc_message, order_to_grpc_message
from google.protobuf.json_format import MessageToDict

class OrderManagementService(ordermanagementservice_pb2_grpc.OrderManagementServiceServicer):
    def __init__(self) -> None:
        super().__init__()
        self._order_repository = OrderRepositoryImplementation()

    def getAll(self, request, context):
        print("getall ", request)
        # Parsing response
        orders = self._order_repository.getAll()
        response_iterator = order_list_to_grpc_message(orders)
    
        # Seding responses
        for response in response_iterator:
            yield response
            
    def get(self, request, context):
        print("get ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        order_id     = request_dict['order_id']
        print(order_id)
        
        # Cancling to repo (could be a DB)
        order = self._order_repository.get(order_id)

        # parsing response
        response = order_to_grpc_message(order)
        
        # Sending response
        return response

    def create(self, request, context):
        print("create ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        product_id   = request_dict['product_id']
        amount       = request_dict['amount']
        
        # Adding to repo (could be a DB)
        order = self._order_repository.create(product_id, amount)
        
        # parsing response
        response = order_to_grpc_message(order)
        
        # Sending response
        return response

    def cancel(self, request, context):
        print("cancel ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        order_id     = request_dict['order_id']
        
        # Cancling to repo (could be a DB)
        is_successful = self._order_repository.cancel(order_id)

        # Sending response
        if is_successful:
            return ordermanagementservice_pb2.OrderResponse(is_successful=True, message="Order canceled succesfully")
        else:
            return ordermanagementservice_pb2.OrderResponse(is_successful=False, message="There was an error")

    def complete(self, request, context):
        print("complete ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        order_id     = request_dict['order_id']
        
        # Cancling to repo (could be a DB)
        is_successful = self._order_repository.complete(order_id)

        # Sending response
        if is_successful:
            return ordermanagementservice_pb2.OrderResponse(is_successful=True, message="Order completed succesfully")
        else:
            return ordermanagementservice_pb2.OrderResponse(is_successful=False, message="There was an error")