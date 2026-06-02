class Book:
    def __init__(self, title, author, isbn, publication_year):
        """Constructor method to initialize the book's attributes."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        """Calculates and returns the age of the book based on the current year 2026."""
        current_year = 2026
        return current_year - self.publication_year

    def get_summary(self):
        """Returns a formatted summary string of the book details."""
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


if __name__ == "__main__":
    book1 = Book(
        title="Harry Potter and the Philosopher's Stone",
        author="J.K. Rowling",
        isbn="978-0747532699",
        publication_year=1997
    )
    
    book2 = Book(
        title="The Alchemist",
        author="Paulo Coelho",
        isbn="978-0062315007",
        publication_year=1988
    )
    
    book3 = Book(
        title="A Man Called Ove",
        author="Fredrik Backman",
        isbn="978-1476738024",
        publication_year=2012
    )

    books_list = [book1, book2, book3]
    
    for i, book in enumerate(books_list, 1):
        print(f"--- BOOK {i} ---")
        print(f"Title:   {book.title}")
        print(f"Author:  {book.author}")
        print(f"Age:     {book.get_age()} years old")
        print(f"Summary: {book.get_summary()}")
        print("\n")