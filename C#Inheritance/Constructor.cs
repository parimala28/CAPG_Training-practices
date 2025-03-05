using System;
class Employee
{
    public string Name { get; set; }
    public double Salary { get; set; }
    public Employee(string name,double salary)
    {
        Name = name;
        Salary = salary;
    }
    public virtual void Display()
    {
        Console.WriteLine($"Name:{Name},Salary:{Salary}");
    }
    
}
class Manager : Employee
{
    public Manager(string name, double salary, double bonus) : base(name, salary)
    {
        Bonus = bonus;

    }
    public double Bonus { get; set; }

    public override void Display()
    {
        base.Display();
        Console.WriteLine($"Bonus:{Bonus}");

    }
}
class Program
{
   static void Main()
   {


   Employee emp = new Employee("pari", 10000);
   emp.Display();
   Manager man = new Manager("pari", 10000, 300);
   man.Display();
 }
}
