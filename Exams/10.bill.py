
# Function to display data
def display(data):
    return f"{data}"


def get_input():   #input
    Total_bill_amount = float(input("Enter total bill: "))
    Number_of_People = int(input("Enter the number of people: "))
    Tip_per = float(input("Enter tip per person: "))
    return Total_bill_amount, Number_of_People, Tip_per

# Function to calculate the last amount per person
def bill(Total_bill_amount, Number_of_People, Tip_per):
    Last = (Total_bill_amount + Tip_per) / Number_of_People
    return Last


def main():
    Total_bill_amount, Number_of_People, Tip_per = get_input()
    Last = bill(Total_bill_amount, Number_of_People, Tip_per)
    print(display(f"Each person should pay: ${Last:.2f}"))

# Calling the main function 
main()

