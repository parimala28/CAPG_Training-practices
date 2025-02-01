class Shape:
    def area(self):
        pass
class Triangle(Shape):
    def __init__(self,height,base):
        self.height=height
        self.base=base 

    def area(self):
        return (0.5)*(self.base*self.height)

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side

c=Triangle(2,5)
s1=Square(5)
print(c.area())
print(s1.area())

               