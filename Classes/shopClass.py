class Shop:
    def __init__(self,itemID,itemName,quantity):
        self.itemID = itemID
        self.itemName = itemName
        self.quantity = quantity
    def buy(self, units):
        self.quantity += units
    def sell(self, units):
        self.quantity -= units
    def total_items():
        return A.quantity + B.quantity
A = Shop("1","A",20)
B = Shop("2","B",30)
print(Shop.total_items())
A.sell(13)
print(Shop.total_items())
B.buy(5)
print(Shop.total_items())