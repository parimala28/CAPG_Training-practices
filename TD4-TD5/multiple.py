class Woman:
    name="pari"
    def Bus(self):

        return "woman can go by bus"
class Man:
    age=30
    def Bike(self):
        return "Man can go by bike"
class Person(Woman,Man):
    size=20.3
    def lady(self):
        return "lady"
person=Person()
print(person.Bus())
print(person.Bike())
print(person.lady())

p=Person()
p=person
print(p.lady())
print(person.name)
print(person.age)
print(person.size)
  