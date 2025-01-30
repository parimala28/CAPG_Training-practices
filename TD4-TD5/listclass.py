class Employee():
    def __init__(self,employee_id,employee_name,employee_age):
       self.__employee_id=employee_id
       self.__employee_name=employee_name
       self.__employee_age=employee_age

    def  set_id(self,employee_id):
        self.__employee_id=employee_id
    def get_id(self):
        return self.__employee_id  

    def set_name(self,employee_name):
        self.__employee_name=employee_name
    def get_name(self):
        return self.__employee_name

    def set_age(self,employee_age):
        self.__employee_age=employee_age
    def get_age(self):
        return self.__employee_age
    
emp=Employee(123,"pari",20)

emp1=emp.get_id()
emp2=emp.get_name()
emp3=emp.get_age()   

L1=[emp1,emp2,emp3]
print(L1)


#-----------------------------------------------------

            
class Employee:
    def __init__(self, employee_id, employee_name, employee_age):
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        self.__employee_age = employee_age

    def get_details(self):
        return f"Employee[ID: {self.__employee_id}, Name: {self.__employee_name}, Age: {self.__employee_age}]"


class Department:
    def __init__(self, dept_id, dept_name):
        self.__dept_id = dept_id
        self.__dept_name = dept_name

    def get_details(self):
        return f"Department[ID: {self.__dept_id}, Name: {self.__dept_name}]"


class Company:
    def __init__(self, company_id, company_name):
        self.__company_id = company_id
        self.__company_name = company_name

    def get_details(self):
        return f"Company[ID: {self.__company_id}, Name: {self.__company_name}]"



emp1 = Employee(101, "Alice", 25)
dept1 = Department(1, "HR")
comp1 = Company(501, "TechCorp")


object_list = [emp1,  dept1,  comp1]
for obj in object_list:
  print(obj.get_details())

#-------------------------------------------

class Employee():
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

emp=Employee(123,"pari",30)
emp1=emp.get_id() 
emp2=emp.get_name()
emp3=emp.get_age()
L1=[emp1,emp2,emp3]
print(L1)
