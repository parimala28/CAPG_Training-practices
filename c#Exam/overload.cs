using System;
public class Calculator
{
    public int Add(int a,int b)
    {
        return a+b;
    }
    public int Add(int a,int b,int c)
    {
        return a+b+c;
    }
    public double Add(double a,double b)
    {
        return a+b;
    }
}
class Program
{
    static void Main()
    {
        Calculator calculator = new Calculator();
        Console.WriteLine("Add two integers: "+calculator.Add(2,3));
        Console.WriteLine("Add three integers: "+calculator.Add(2,3,4));
        Console.WriteLine("Add two doubles: "+calculator.Add(2.5,3.5));
    }
}