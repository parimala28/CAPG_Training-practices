using System;

class BankAccount
{
    private decimal balance; 

    public BankAccount(decimal initialBalance)
    {
        if (initialBalance <0)
        {
            throw new ArgumentException("Initial balance cannot be negative.");
        }
        balance = initialBalance;
    }

    public void Deposit(decimal amount)
    {
        if (amount >0)
        {
            balance +=amount;
            Console.WriteLine($"Deposited: {amount:C}. New Balance: {balance:C}");
        }
        else
        {
            Console.WriteLine("Deposit amount must be positive.");
        }
    }

    public void Withdraw(decimal amount)
    {
        if (amount > 0 && amount <=balance)
        {
            balance -=amount;
            Console.WriteLine($"Withdrawn: {amount:C}. Remaining Balance: {balance:C}");
        }
        else if (amount >balance)
        {
            Console.WriteLine("Insufficient balance.");
        }
        else
        {
            Console.WriteLine("Withdrawal amount must be positive.");
        }
    }

    public decimal GetBalance()
    {
        return balance;
    }
}

class Program
{
    static void Main()
    {
        BankAccount account = new BankAccount(500);
        account.Deposit(200);
        account.Withdraw(100);
        account.Withdraw(700);
        Console.WriteLine($"Final Balance: {account.GetBalance():C}");
    }
}

