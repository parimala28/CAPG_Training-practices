import math

def display(data):
    print(f"{data}")


def get_input():
    
    name = input("Enter name: ")
    s1 = int(input("Enter 1st Subject marks: "))
    s2 = int(input("Enter 2nd Subject marks: "))  
    s3 = int(input("Enter 3rd Subject marks: "))  
    s4 = int(input("Enter 4th Subject marks: "))  
    s5 = int(input("Enter 5th Subject marks: "))  
    return name, s1, s2, s3, s4, s5                   #input function

# Function to calculate sum and percentage
def marks(s1, s2, s3, s4, s5):
    total = s1 + s2 + s3 + s4 + s5
    percentage = (total / 500) * 100
    return total, percentage

# Function for grade
def grades(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


def main():
    name, s1, s2, s3, s4, s5 = get_input()  
    total, percentage = marks(s1, s2, s3, s4, s5)  
    grade = grades(percentage)                  # Get grade based on percentage
    
    # Display results
    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {total}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

# Calling the main function 
main()

