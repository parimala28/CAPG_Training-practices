def pattern(n, reverse=False):
    if reverse:
        # Generate reverse pattern
        for i in range(n, 0, -1):
            print('*' * i)
    else:
        # Generate normal pattern
        for i in range(1, n + 1):
            print('*' * i)

# Main function to get user input and display the pattern
def main():
    n = int(input("Enter the number of rows: "))
    reverses = input("want reverse? (yes/no): ").lower()
    
    # Check if the user wants to print in reverse
    if reverses == 'yes':
        pattern(n, reverse=True)
    else:
        pattern(n)

# Call the main function
main()
