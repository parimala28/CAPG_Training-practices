using System;
public class Person
{
    public string Name {get; set;}
    public int Age {get; set;}
    public virtual string GetDetails()
    {
        return $"Name:{Name},Age:{Age}";
    }
}
public class Student : Person
{
    public string StudentID {get; set;}
    public override string GetDetails()
    {
        return $"Name: {Name},Age:{Age},Student ID: {StudentID}";
    }
}
public class Teacher : Person
{
    public string Subject {get; set;}

    public override string GetDetails()
    {
        return $"Name: {Name},Age: {Age},Subject: {Subject}";
    }
}
public class Program
{
    public static void Main()
    {
        Person person=new Person{Name="John Doe",Age=45};
        Person student=new Student{Name="Jane Smith",Age=20,StudentID="S12345"};
        Person teacher=new Teacher{Name="Mr. Brown",Age=50,Subject="Mathematics"};

        Console.WriteLine(person.GetDetails());
        Console.WriteLine(student.GetDetails());
        Console.WriteLine(teacher.GetDetails());
    }
}