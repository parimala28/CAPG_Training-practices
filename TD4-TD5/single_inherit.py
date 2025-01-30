# class Parent():
#     def display_parent(self):
#         print("this is parent class.")
# class Child(Parent):
#     def display_child(self):
#         print("this is the child class.")  
# child=Child()
# child.display_parent()
# child.display_child()


class parent:
    def __init__(self):
        self.bigNose='5cm'
    def display_parent(self):
        print("The parent class.")
class Child(parent):
    def __init__(self):
        super().__init__()
    def display_child(self):
        print("This is child class.")
child=Child()
child.display_child()
child.display_parent()
print("the nose:",child.bigNose)                    

# p=parent()
# ch=Child()
# p=ch