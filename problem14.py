class Order():
    def __init__(self):
        self.order_Ids = []  
    
    
    def record(self, order_id):

        self.order_Ids.append(order_id)
    

    def get_last(self, i):

        return self.order_Ids[len(self.order_Ids) - 1 - i]


if __name__ == "__main__":
    eCommerceOrders = Order()
    for i in range(1, 101):  
        eCommerceOrders.record(i)
    
    print(eCommerceOrders.get_last(20))     
    print(eCommerceOrders.get_last(60))     
