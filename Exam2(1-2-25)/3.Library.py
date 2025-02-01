class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def display_book_details(self):
        print(f"The book title is: {self.title}")
        print(f"The author of book is: {self.author}")
        print(f"The book number is: {self.isbn}")   
book=Book("The Free Bird","james stone",123)
book.display_book_details()        