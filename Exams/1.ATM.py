def c_b(balance):
    print(f"Your current balance is: {balance}")     #check balace


def d_m(balance):    #deposit money
    a=float(input("Enter the amount to deposit: "))
    if a<=0:
        print("negative amount is invalid")
    else:
        balance+=a
        print(f"{a} has been deposited. Your new balance is: {balance}")
    return balance


def w_m(balance):       #withdraw money
    a=float(input("Enter the amount to withdraw: "))
    if a<=0:
        print("positive number should type.")
    elif a>balance:
        print("Insufficient balance to withdraw.")
    else:
        balance-=a
        print(f"{a} has been withdrawn. Your new balance is: {balance}")
    return balance


def ATM():
    balance=1000  # Initial balance
    while True:
        print("\nATM Simulation")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        m=int(input("Select an options: "))
        if m == 1:
            c_b(balance)
        elif m == 2:
            balance=d_m(balance)
        elif m==3:
            balance = w_m(balance)
        elif m == 4:
            print("Thank you .")
            break
        else:
            print("Invalid choice.")


# Run the ATM simulation
ATM()
