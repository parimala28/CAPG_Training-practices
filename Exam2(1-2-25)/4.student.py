class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display_details(self):
        print(f"The student name is: {self.name}")
        print(f"The roll number of student is: {self.roll_no}")

name=input("Enter the name:")
roll_no=input("Enter the roll number:")

student=Student(name,roll_no)
student.display_details()            