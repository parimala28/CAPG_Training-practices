using System;
abstract class Animal
{
    public abstract void MakeSound();
    
}
class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Dog barks");
    }
}
class Cat : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Cat meows");
    }
}
class Program
{
    static void Main()
    {
        Dog dog = new Dog();
        dog.MakeSound();
        Cat cat = new Cat();
        cat.MakeSound();
    }
}

