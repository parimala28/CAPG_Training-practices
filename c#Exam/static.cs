using System;
namespace BankingSystem
{
    public class Bank
    {
        public string AccountHolder {get;set;}
        public double Balance {get;set;}
        public static double InterestRate {get;private set;}=5.0;
        public Bank(string accountHolder,double balance)
        {
            AccountHolder=accountHolder;
            Balance=balance;
        }

        public static void SetInterestRate(double newRate)
        {
            InterestRate=newRate;
        }

        public void DisplayAccountInfo()
        {
            Console.WriteLine($"Account Holder: {AccountHolder}, Balance: {Balance}, Interest Rate: {InterestRate}%");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Bank account1 = new Bank("Pari", 10000);
            Bank account2 = new Bank("ram", 20000);

            account1.DisplayAccountInfo();
            account2.DisplayAccountInfo();

            
            Bank.SetInterestRate(6.4);
            Console.WriteLine("\nAfter Changing Interest Rate:");

            account1.DisplayAccountInfo();
            account2.DisplayAccountInfo();
        }
    }
}
