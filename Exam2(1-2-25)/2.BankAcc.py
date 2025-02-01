class BankAccount:
    def __init__(self,Account_Holder,balance=0):
        self.Account_Holder=Account_Holder
        self.balance=balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"The deposited money is ${amount:.2f}")
        else:
            print("deposit the positive number.") 
            
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient amount is present in account.")
        elif amount <=0 :
            print("The withdraw money should be positive.")
        else:
            self.balance -= amount
            print(f"withdraw ${amount:.2f}") 

    def display_balance(self):
        print(f"The {self.Account_Holder}'s Account Balance: ${self.balance:.2f}")        

bank=BankAccount("pari",500)
bank.deposit(300)
bank.withdraw(200)
bank.withdraw(800)
bank.display_balance()

        