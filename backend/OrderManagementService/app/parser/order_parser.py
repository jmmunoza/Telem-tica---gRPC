from app.domain.entities.product import Product
from app.domain.entities.order import Order
from app.grpc_generated.ordermanagementservicegrpc import ordermanagementservice_pb2
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2

def dict_to_product(dict):
    print(dict)
    return Product(
        dict["product_id"],
        dict["name"],
        dict["price"],
        dict["stock"]
    )
    
def order_list_to_grpc_message(list):
    dict_list = []
    
    for order in list:
        item = order_to_grpc_message(order)
        
        dict_list.append(item)
   
    return dict_list

def order_to_grpc_message(order):
    if order is None:
        return ordermanagementservice_pb2.Order()
    
    return ordermanagementservice_pb2.Order(
            order_id = order.getId(), 
            produtct_id = order.getProductId(),
            amount = order.getAmount()
    )