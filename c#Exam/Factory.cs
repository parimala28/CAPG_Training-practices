using System;
public abstract class Vehicle
{
    public abstract void Drive();
}public class Car : Vehicle
{
    public override void Drive()
    {
        Console.WriteLine("Driving a Car!");
    }
}public class Bike : Vehicle
{
    public override void Drive()
    {
        Console.WriteLine("Riding a Bike!");
    }
}public class VehicleFactory
{
    public static Vehicle CreateVehicle(string type)
    {
        switch (type.ToLower())
        {
            case "car":
                return new Car();
            case "bike":
                return new Bike();
            default:
                throw new ArgumentException("Invalid vehicle type.");
        }
    }
}

// Main program
class Program
{
    static void Main(string[] args)
    {
        Vehicle car=VehicleFactory.CreateVehicle("car");
        car.Drive(); 
        Vehicle bike=VehicleFactory.CreateVehicle("bike");
        bike.Drive(); 
        

        
    }
}