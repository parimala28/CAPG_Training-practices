class Cat():
    def sound(self):
        print("Meow")

class Dog():
    def sound(self):
        print("Bark")

class Duck():
    def sound(self):
        print('Quack')        

for animal in [Cat(),Dog(),Duck()]:
    animal.sound()               
