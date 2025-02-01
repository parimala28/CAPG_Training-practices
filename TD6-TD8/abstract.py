from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod      #abstractmethod without body
    def disp(self):
        pass
    def show(self):   #concrete method with body
        print("Concrete Method")

    @abstractmethod
    def set_pancard(self,pancard):
        pass 

class Son(Father):
    def __init__(self):
        self.pancard=None
    def disp(self):
        print("son is implemented in abstract class")
    def set_pancard(self, pancard):
        self.pancard=pancard
        print("the pan number is",self.pancard)   

class Daughter(Father):
    def __init__(self):
        self.pancard=None
    def disp(self):
        print("Daughter is implementing the abstract class")
    def set_pancard(self, pancard):
        self.pancard=pancard
        print("the daughter pan card number is",self.pancard)   

s=Son()
s.disp()  
s.show()
s.set_pancard("i2ncchd")

d=Daughter()
d.disp()
d.show()
d.set_pancard("018ks")
        