def printStrongNess(input):
    n = len(input)

    # Checking for different character types in the string
    Lower = False
    Upper = False
    Digit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

    for i in range(n):
        if input[i].islower():
            Lower = True
        if input[i].isupper():
            Upper = True
        if input[i].isdigit():
            Digit = True
        if input[i] not in normalChars:
            specialChar = True

    # Strength of the password
    print("Strength of password: ", end="")
    if Lower and Upper and Digit and specialChar and n >= 8:
        print("Strong")
    elif (Lower or Upper) and specialChar and n >= 6:
        print("Moderate")
    else:
        print("Weak")


if __name__ == "__main__":
    input = input("Enter your password: ")  
    printStrongNess(input)
