using System;

namespace SecuritySystemDemo
{
    public sealed class SecuritySystem
    {
        public string SystemName {get;set;}
        public SecuritySystem(string systemName)
        {
            SystemName=systemName;
        }
        public void Authenticate()
        {
            Console.WriteLine($"{SystemName} authentication successful.");
        }
    }
class Program
    {
        static void Main(string[] args)
        {
            SecuritySystem security=new SecuritySystem("Main Gate");
            security.Authenticate();
        }
    }
}
