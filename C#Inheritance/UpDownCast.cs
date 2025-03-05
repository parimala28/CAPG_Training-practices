using System;
class Person
{
    public void Greet()
    {
        Console.WriteLine("Person is greeting");
    }
}
class Student : Person
{
    public void Study()
    {
        Console.WriteLine("Student is studying");
    }
}
class Program
{
    static void Main()
    {
        
        Student student = new Student();
        student.Greet();
        student.Study();
        Person person = student; 
        person.Greet();
        if (person is Student s)
        {
            s.Study(); 
            
        }
        else
        {
            Console.WriteLine("Downcasting failed.");
        }
    }
}
