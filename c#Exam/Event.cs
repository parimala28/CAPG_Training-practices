using System;

namespace EventHandlingDemo
{
    public class Button
    {
        public delegate void ClickHandler();
        public event ClickHandler OnClick;

        public void Click()
        {
            Console.WriteLine("Button clicked!");
            OnClick?.Invoke();
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Button button =new Button();
            button.OnClick += () =>Console.WriteLine("Button event triggered!");
            button.Click();
        }
    }
}
