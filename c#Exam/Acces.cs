using System;
namespace RoleBasedAccessSystem
{
    public class User
    {
        public string Username {get; set;}
        public string Role {get; set;}

        public User(string username,string role)
        {
            Username=username;
            Role=role;
        }

        public virtual void AccessControl()
        {
            Console.WriteLine("Access control for user.");
        }
    }
    public class Admin : User
    {
        public Admin(string username) : base(username,"Admin")
        {
        }

        public override void AccessControl()
        {
            Console.WriteLine("Admin has access to all features.");
        }
    }
    public class Customer : User
    {
        public Customer(string username) :base(username,"Customer")
        {
        }

        public override void AccessControl()
        {
            Console.WriteLine("Customer has limited access.");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            User admin =new Admin("adminUser");
            User customer =new Customer("customerUser");

            admin.AccessControl();
            customer.AccessControl();
        }
    }
}