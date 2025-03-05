using System;
using System.Collections.Generic;
namespace ObserverPattern
{
    public interface IObserver
    {
        void Notify(string message);
    }
    public class EmailNotifier : IObserver
    {
        public void Notify(string message)
        {
            Console.WriteLine($"Email:{message}");
        }
    }
    public class SMSNotifier : IObserver
    {
        public void Notify(string message)
        {
            Console.WriteLine($"SMS:{message}");
        }
    }

    public class NotificationService
    {
        private List<IObserver> observers=new List<IObserver>();

        public void Subscribe(IObserver observer)
        {
            observers.Add(observer);
        }

        public void NotifyAll(string message)
        {
            foreach (var observer in observers)
            {
                observer.Notify(message);
            }
        }
    }
class Program
    {
        static void Main()
        {
            NotificationService service=new NotificationService();
            service.Subscribe(new EmailNotifier());
            service.Subscribe(new SMSNotifier());

            service.NotifyAll("New message received!");
        }
    }
}
