using System;
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    
    public Product(string name,double price)
    {
        Name=name;
        Price=price;
    }
    
    public virtual double GetDiscountedPrice()
    {
        return Price; 
        
    }
    
    public void Display()
    {
        Console.WriteLine($"Product: {Name},Price: {Price:C},Discounted Price: {GetDiscountedPrice():C}");
    }
}
class ElectronicProduct : Product
{
    public ElectronicProduct(string name,double price) : base(name,price) { }
    
    public override double GetDiscountedPrice()
    {
        return Price*0.9; 
    }
}
class ClothingProduct : Product
{
    public ClothingProduct(string name,double price) : base(name,price) { }
    
    public override double GetDiscountedPrice()
    {
        return Price*0.8; 
    }
}

// Main Program
class Program
{
    static void Main()
    {
        Product phone=new ElectronicProduct("phone", 9000);
        phone.Display();
        
        Product frock=new ClothingProduct("Long frock", 5000);
        frock.Display();
    }
}
