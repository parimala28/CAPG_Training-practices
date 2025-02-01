from abc import ABC,abstractmethod
class ICalculate(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def subtract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass

class BaseCalculator(ICalculate):
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    
bc=BaseCalculator()
print(bc.add(2,3))
print(bc.subtract(8,3))
print(bc.multiply(8,2))
print(bc.divide(10,2))

