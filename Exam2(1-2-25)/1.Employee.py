class Employee:
    def __init__(self,name,emp_id,department):
        self.name=name
        self.emp_id=emp_id
        self.department=department
        
    def info(self):
        print(f"The name of employee is: {self.name}")
        print(f"The id of the employee is: {self.emp_id}")
        print(f"The department of employee is: {self.department}")

name=input("Enter the name: ") 
emp_id=input("Enter the id of employee:")
department=input("Enter the department name: ")

emp=Employee(name,emp_id,department)
emp.info()         