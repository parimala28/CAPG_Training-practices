# Function to check if a year is a leap year
def leap(num):
    if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
        return True
    else:
        return False

# Main function
def main():
    
    while True:
        # Get year from the user
       
        n=int(input("Ebter a year: "))
        if n == 0:
            print("Exit")
            break
        
         # Check if the year is a leap year
        if leap(n):
            print(f"{n} is a leap year.")
        else:
            print(f"{n} is not a leap year.")
main()
