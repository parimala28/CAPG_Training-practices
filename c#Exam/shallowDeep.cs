using System;
public class Manager
{
    public string Name {get;set;}
    public Manager(string name)
    {
        Name=name;
    }
}

public class Department : ICloneable
{
    public string DepartmentName {get;set;}
    public Manager Manager {get;set;}

    public Department(string departmentName,Manager manager)
    {
        DepartmentName=departmentName;
        Manager=manager;
    }

    // Shallow Copy
    public object Clone()
    {
        return this.MemberwiseClone();
    }

    // Deep Copy
    public Department DeepCopy()
    {
        Department deepCopyDepartment=(Department)this.MemberwiseClone();
        deepCopyDepartment.Manager=new Manager(this.Manager.Name);
        return deepCopyDepartment;
    }
}

class Program
{
    static void Main()
    {
        Manager manager1=new Manager("John Doe");
        Department dept1=new Department("HR", manager1);

        // Shallow Copy
        Department shallowCopyDept=(Department)dept1.Clone();
        // Deep Copy
        Department deepCopyDept=dept1.DeepCopy();

        Console.WriteLine("Original Manager Name: "+dept1.Manager.Name);
        Console.WriteLine("Shallow Copy Manager Name: "+shallowCopyDept.Manager.Name);
        Console.WriteLine("Deep Copy Manager Name: "+deepCopyDept.Manager.Name);

        dept1.Manager.Name = "Jane Smith";

        Console.WriteLine("Original Manager Name: "+dept1.Manager.Name);
        Console.WriteLine("Shallow Copy Manager Name: "+shallowCopyDept.Manager.Name);
        Console.WriteLine("Deep Copy Manager Name: "+deepCopyDept.Manager.Name);
    }
}