class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def check_availability(self,quantity):
        if quantity <= self.stock:
            return True
        else:
            return False

    def purchase(self,quantity):
        if self.check_availability(quantity):
            self.stock -= quantity
            return True
        else:
            False

    def display(self):
        print(f"product: {self.name}")
        print(f"The price: ${self.price:.2f}")
        print(f"stock: {self.stock}")

product=Product("mobiles",20000,20)
product.display()

req_quantity = int(input("\nEnter quantity to purchase: "))

if product.check_availability(req_quantity):
    product.purchase(req_quantity)
else:
    print("Insufficient stock!")

product.display()