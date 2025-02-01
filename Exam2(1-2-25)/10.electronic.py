class Electronic:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display_ele(self):
        print(f"The name : {self.name} ")
        print(f"The price is: {self.price}")

class Moblie_Devices(Electronic):
    def __init__(self,name,price,size):
        super().__init__(name,price)
        self.size=size
    def display_md(self):
       super().display_ele()
       print(f"The size is: {self.size}")

class Smart_Phones(Moblie_Devices):
    def __init__(self,name,price,size,ram):
        super().__init__(name,price,size)
        self.ram=ram
    def display_sp(self):
        super().display_md()
        print(f"The ram is: {self.ram}") 

sp=Smart_Phones("Iphone",50000,12.1,256)
sp.display_sp()        
