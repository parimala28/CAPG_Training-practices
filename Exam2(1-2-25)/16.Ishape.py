from abc import ABC ,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        return self.length*self.width

class Circle(IShape):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius*self.radius                


r=Rectangle(2,4)
print(r.calculate_area())
c=Circle(3)
print(c.calculate_area())
