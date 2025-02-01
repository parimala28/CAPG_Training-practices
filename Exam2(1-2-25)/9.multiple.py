class Car:
    def move(self):
        print("The car will move on Road ")

class Airplane:
    def move(self):
        print("The Airplane will fly in air")

class FlyingCar(Car,Airplane):
    def move(self):
        print("The flyingcar will move on road and fly in air")


fc=FlyingCar()
fc.move()
Car().move()
Airplane().move()