class product:
    def __init__(self, productname, price, discount, GST, Quantity):
        self.productname = productname
        self.price = price
        self.discount = discount
        self.GST = GST
        self.Quantity = Quantity
    def display(self):
        print(f"product name is: {self.productname}" ) 
        print(f"price is: {self.price}" )
        print(f"discount is: {self.discount}" )
        print(f"GST is: {self.GST}" )
        print(f"Quantity is: {self.Quantity}" )
P1=product("laptop", 45000, 5000, 18, 2)
P1.display()
P2=product("mobile", 40000, 3000, 12, 3)
P2.display()
P3=product("headphones", 4000, 500, 5, 5)
P3.display()
P4=product("smartwatch", 10000, 1000, 8, 4)
P4.display()
P5=product("tablet", 20000, 2000, 10, 6)
P5.display()