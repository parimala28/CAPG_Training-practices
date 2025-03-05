using System;
public class Vehicle
{
    public virtual void Start()
    {
        Console.WriteLine("Vehicle is starting");
    }
}
public class Car : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Car is starting");
    }
}
public class Bike : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Bike is starting");
    }
}
public class Program
{
    public static void Main()
    {
        Vehicle myVehicle = new Vehicle();
        myVehicle.Start();

        Vehicle myCar = new Car();
        myCar.Start();

        Vehicle myBike = new Bike();
        myBike.Start();
    }
}