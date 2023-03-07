class Product:
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name       = name
        self._price      = price
        self._stock      = stock
        
    def getId(self):
        return self._product_id
    
    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price
    
    def getStock(self):
        return self._stock
    
    def __str__(self) -> str:
        return str({
            'product_id': self.getId(),
            'name': self.getName(),
            'price': self.getPrice(),
            'stock': self.getStock()
        })