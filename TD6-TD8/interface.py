from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"   


d=Dog()
c=Cat()
  
print(d.make_sound()) 
print(c.make_sound())   