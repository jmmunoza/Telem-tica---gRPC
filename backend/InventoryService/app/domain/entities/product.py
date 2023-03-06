class Product:
    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self._name       = name
        self._price      = price
        
    def getId(self):
        return self._product_id
    
    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price
    
    def __str__(self) -> str:
        return str({
            'product_id': self.getId(),
            'name': self.getName(),
            'price': self.getPrice()
        })