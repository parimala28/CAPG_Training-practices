using System;
class Vehicle
{
    public string Brand { get; set; }
    public int Speed { get; set; }

    public Vehicle(string brand, int speed)
    {
        Brand = brand;
        Speed = speed;
    }

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"Brand:{Brand},Speed:{Speed} km/h");

    }

}
class Car : Vehicle
{
    public Car(string brand, int speed) : base(brand, speed) { }
    public override void  DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("Car is going in the speed of 200 km/h");
    }
}
class Bike : Vehicle
{
    public Bike(string brand, int speed) : base(brand, speed) { }
    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine("Bike is going in the speed of 100 km/h");
    }
}
class Program
{
   static void Main()
   {
       Car car = new Car("KIA", 200);
       Bike bike = new Bike("BMW", 100);
       car.DisplayInfo();
       bike.DisplayInfo();
   }}
    