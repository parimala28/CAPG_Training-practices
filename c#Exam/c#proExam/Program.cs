﻿using System;

abstract class Shape
{
    public abstract double CalculateArea();
}

class Circle : Shape
{
    public  double radius{get;set;}

    public Circle(double radius)
    {
        this.radius = radius;
    }

    public override double CalculateArea()
    {
        return 3.14 * radius * radius;
    }
}

class Rectangle : Shape
{
    public  double width{get;set;}
    public double height{get;set;}

    public Rectangle(double width, double height)
    {
        this.width = width;
        this.height = height;
    }

    public override double CalculateArea()
    {
        return width * height;
    }
}

class Program
{
    static void Main()
    {
        Shape circle = new Circle(10);
        Console.WriteLine("Area of Circle: "+circle.CalculateArea());

        Shape rectangle = new Rectangle(10,20);
        Console.WriteLine("Area of Rectangle: "+rectangle.CalculateArea());
    }
}