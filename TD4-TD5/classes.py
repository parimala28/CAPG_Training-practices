class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"This car is a :{self.brand} {self.model}")
car1=Car("Toyota","corolla")
car2=Car("Honda","civic") 
car1.display()
car2.display() 



class Employee:
    def __init__(self,name,salary,allow,ded,transportcharges):
        self.__name=name
        self.__salary=salary
        self.__allow=allow
        self.__deduct=ded
        self.__transportcharges=transportcharges
     


    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name 
               
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    
    def set_allowance(self,allow):
        self.__allow=allow
    def get_allowance(self):
        return self.__allow

    def set_transportcharges(self,transportcharges):
        self.__transportcharges=transportcharges
    def get_transportcharges(self):
        return self.__transportcharges      
    
    def set_deduct(self,ded):
        self.__deduct=ded
    def get_deduct(self):
        return self.__deduct  

    def net_salary(self):
        return self.__salary + (self.__allow + self.__transportcharges) - self.__deduct    

        
    
# emp=Employee("pari",40000,2000,7000,3000)
# print("employee name:",emp.get_name())
# print("salary before update:",emp.get_salary())
# print("the net salary:",emp.net_salary())

emp=input("enter the name")
emp.get_name()

