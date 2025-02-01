class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display_per(self):
        print(f"The  name is: {self.name}")
        print(f"The age  is: {self.age}")    

class Employee(Person):
    def __init__(self,name,age,emp_id):
        super().__init__(name,age)  
        self.id=emp_id

    def display_emp(self):
        super().display_per()
        print(f"The id is: {self.id}")    

class Manager(Employee):
    def __init__(self,name,age,emp_id,department):
        super().__init__(name,age,emp_id) 
        self.department=department

    def display_man(self):
        super().display_emp()
        print(f"The department name is: {self.department}")    

    def approve_leave(self):
        print(f"The leave is approved for {self.name}.")


m = Manager("Pari",50,"E123","HR")



m.display_man()
m.approve_leave()
