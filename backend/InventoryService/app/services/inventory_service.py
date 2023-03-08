from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2_grpc
from app.adapter.product_repository_implementation import ProductRepositoryImplementation

# Parser
from google.protobuf.json_format import MessageToDict
from app.parser.product_parser import dict_to_product, product_list_to_grpc_message, product_to_grpc_message


class InventoryService(inventoryservice_pb2_grpc.InventoryServiceServicer):
    def __init__(self) -> None:
        super().__init__()
        self._product_repository = ProductRepositoryImplementation()

    def getAll(self, request, context):
        print("getall ", request)
        # Parsing response
        products = self._product_repository.getAll()
        response_iterator = product_list_to_grpc_message(products)
    
        # Seding responses
        for response in response_iterator:
            yield response
            

    def add(self, request, context):
        print("add ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        name         = request_dict['name']
        stock        = request_dict['stock']
        price        = request_dict['price']
        
        # Adding to repo (could be a DB)
        product = self._product_repository.add(name, price, stock)

        # Parsing response
        response = product_to_grpc_message(product)
        
        # Sending response
        return response

    def get(self, request, context):
        print("get ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        product_id = request_dict['product_id']
        
        # Retrieving product from repo (could be a DB)
        product = self._product_repository.get(product_id)
        
        # Parsing response
        response = product_to_grpc_message(product)
        return response

    def delete(self, request, context):
        print("delete ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        product_id = request_dict['product_id']

        # Adding to repo (could be a DB)
        is_successful = self._product_repository.delete(product_id)

        # Sending response
        if is_successful:
            return inventoryservice_pb2.ProductResponse(is_successful=True, message="Product deleted succesfully")
        else:
            return inventoryservice_pb2.ProductResponse(is_successful=False, message="There was an error")
        
    def update(self, request, context):
        print("update ", request)
        # Parsing request
        request_dict = MessageToDict(request, preserving_proto_field_name=True)
        product      = dict_to_product(request_dict) 

        # Updating to repo (could be a DB)
        is_successful = self._product_repository.update(product)

        # Sending response
        if is_successful:
            return inventoryservice_pb2.ProductResponse(is_successful=True, message="Product updated succesfully")
        else:
            return inventoryservice_pb2.ProductResponse(is_successful=False, message="There was an error")
