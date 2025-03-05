using System;
class Account{
    public virtual void CalculateInterest(){
        Console.WriteLine("Calculating interest");
    }
}
class SavingsAccount : Account{
    public sealed override void CalculateInterest(){
        Console.WriteLine("Calculating interest for savings account");
    }

}
class Program{
    static void Main(){
        SavingsAccount sa = new SavingsAccount();
        sa.CalculateInterest();
    }
}