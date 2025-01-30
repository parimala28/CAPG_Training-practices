class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius 

    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side

c=Circle(2)
s1=Square(5)
print(c.area())
print(s1.area())

               