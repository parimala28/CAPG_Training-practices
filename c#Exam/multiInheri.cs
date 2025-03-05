using System;
interface IPrintable
{
    void Print();
}
interface ISerializable
{
    void Save();
}
class Report : IPrintable, ISerializable
{
    public void Print()
    {
        Console.WriteLine("Printing details");
    }

    public void Save()
    {
        Console.WriteLine("Saving  to file");
    }
}
class Program
{
    static void Main()
    {
        Report report =new Report();
        report.Print();  
        report.Save();   
        
    }
}
