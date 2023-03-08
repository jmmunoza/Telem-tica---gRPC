class Order:
    def __init__(self, order_id, product_id, amount):
        self._order_id = order_id
        self._product_id = product_id
        self._amount = amount

    def getId(self):
        return self._order_id

    def getProductId(self):
        return self._product_id

    def getAmount(self):
        return self._amount
    
    def __str__(self) -> str:
        return str({
            'order_id': self.getId(),
            'product_id': self.getProductId(),
            'amount': self.getAmount()
        })