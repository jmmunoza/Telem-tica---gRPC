from app.domain.entities.product import Product
from app.grpc_generated.inventoryservicegrpc import inventoryservice_pb2

def dict_to_product(dict):
    print(dict)
    return Product(
        dict["product_id"],
        dict["name"],
        dict["price"],
        dict["stock"]
    )
    
def product_list_to_grpc_message(list):
    dict_list = []
    
    for product in list:
        item = product_to_grpc_message(product)
        
        dict_list.append(item)
   
    return dict_list

def product_to_grpc_message(product):
    if product is None:
        return inventoryservice_pb2.Product()
    
    return inventoryservice_pb2.Product(
            product_id = product.getId(), 
            name = product.getName(),
            price = product.getPrice(),
            stock = product.getStock()
    )