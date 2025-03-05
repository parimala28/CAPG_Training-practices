using System;
namespace ConstructorOverloadingLibrary
{
    public class Book
    {
        public string Title {get; set;}
        public string Author {get; set;}
        public string ISBN {get; set;}

        
        public Book()
        {
            Title="Unknown Title";
            Author="Unknown Author";
            ISBN="N/A";
        }
        public Book(string title, string author)
        {
            Title=title;
            Author=author;
            ISBN="N/A";
        }
        public Book(string title,string author,string isbn)
        {
            Title=title;
            Author=author;
            ISBN=isbn;
        }
        public void Display()
        {
            Console.WriteLine($"Title: {Title},Author: {Author},ISBN: {ISBN}");
        }
    }
    class Program
    {
        static void Main()
        {
            Book book1=new Book();
            Book book2=new Book("The Great ", "F. Scott Fitzgerald");
            Book book3=new Book("1984", "George Orwell", "123-4567891234");

            book1.Display();
            book2.Display();
            book3.Display();
        }
    }
}
