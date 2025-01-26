
def loan():
    salary = int(input("Enter the salary: "))
    age = int(input("Enter the age: "))
    cs = int(input("Enter the score: "))
    
    # condition checking using 'and' operator
    if salary >= 50000 and age >= 20 and cs >= 10:
        return "Loan approval"
    else:
        return "Loan not approval"

# Calling the function and printing the result
result = loan()
print(result)
