using System;

namespace StrategyPattern
{
    
    public interface IDiscountStrategy
    {
        double ApplyDiscount(double amount);
    }
    public class NoDiscount : IDiscountStrategy
    {
        public double ApplyDiscount(double amount) => amount;
    }
    public class PercentageDiscount : IDiscountStrategy
    {
        private readonly double _percentage;
        public PercentageDiscount(double percentage) => _percentage = percentage;
        public double ApplyDiscount(double amount) => amount - (amount * _percentage /100);
    }

       public class FixedAmountDiscount : IDiscountStrategy
    {
        private readonly double _discountAmount;
        public FixedAmountDiscount(double discountAmount) => _discountAmount =discountAmount;
        public double ApplyDiscount(double amount) => Math.Max(amount - _discountAmount, 0);
    }

   
    public class ShoppingCart
    {
        private IDiscountStrategy _discountStrategy;
        public void SetDiscountStrategy(IDiscountStrategy discountStrategy)
        {
            _discountStrategy =discountStrategy;
        }

        public double CalculateTotal(double amount)
        {
            return _discountStrategy.ApplyDiscount(amount);
        }
    }

    class Program
    {
        static void Main()
        {
            ShoppingCart cart =new ShoppingCart();
            
            cart.SetDiscountStrategy(new NoDiscount());
            Console.WriteLine("Total (No Discount): " +cart.CalculateTotal(100));

            cart.SetDiscountStrategy(new PercentageDiscount(10));
            Console.WriteLine("Total (10% Discount): " +cart.CalculateTotal(100));

            cart.SetDiscountStrategy(new FixedAmountDiscount(15));
            Console.WriteLine("Total ($15 Discount): " +cart.CalculateTotal(100));
        }
    }
}
