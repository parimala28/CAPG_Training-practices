# Function to generate multiplication table
def table(num, start, end):
    print(f"Multiplication Table for {num}:")
    for i in range(start, end + 1):
        print(f"{num} x {i} = {num * i}")


def main():
    # Get user input
    num = int(input("Enter the number: "))
    start = int(input("Enter the starting range: "))
    end = int(input("Enter the ending range: "))
    
    # Generate and display the table
    table(num, start, end)

# Calling the main function to execute the program
main()
