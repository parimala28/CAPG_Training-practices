using System;
namespace DataHidingWithProperties
{
    public class Student
    {
        private string name="Unknown"; 
        private int rollNo=0; 

        public string Name
        {
            get => name;
            set => name =string.IsNullOrWhiteSpace(value) ? "Unknown" : value;
        }

        public int RollNo
        {
            get => rollNo;
            set => rollNo = value < 0 ? 0 : value;
        }

        public void Display()
        {
            Console.WriteLine($"Student Name: {Name}, Roll No: {RollNo}");
        }
    }

    class Program
    {
        static void Main()  
        {
            Student student =new Student {Name = "John",RollNo = 10};
            student.Display();
        }
    }
}
