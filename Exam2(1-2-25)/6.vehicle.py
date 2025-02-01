class Vehicle:
    def display_vehicle(self):
        print("The vehicle List is:")

class Car(Vehicle):
    def display_car(self):
        print("This is car.")

class ElectricCar(Car):
    def display_Electric_car(self):
        print("This is Electric Car.")        

class Bike(Vehicle):
    def display_bike(self):
        print("This is bike.")
b=Bike()
ec=ElectricCar()

b.display_vehicle()
ec.display_car()
ec.display_Electric_car()
b.display_bike()        
