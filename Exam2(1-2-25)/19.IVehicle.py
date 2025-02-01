from abc import ABC ,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(IVehicle):
    def start_engine(self):
        return "The car engine started."
    def stop_engine(self):
        return "The car engine stopped."
    
class Bike(IVehicle):
    def start_engine(self):
        return "The bike engine started."
    def stop_engine(self):
        return "The bike engine stopped."
    
class Truck(IVehicle):
    def start_engine(self):
        return "The Truck engine started."
    def stop_engine(self):
        return "The Truck engine stopped."    

c=Car()
print(c.start_engine())
print(c.stop_engine())
b=Bike()
print(b.start_engine())
print(b.stop_engine())
t=Truck()
print(t.start_engine())
print(t.stop_engine())          