# library_system.py

class Book:
    """Base class for all books."""
    
    def __init__(self, title, author):
        """Initialize book attributes.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for electronic books."""
    
    def __init__(self, title, author, file_size):
        """Initialize eBook attributes.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for physical printed books."""
    
    def __init__(self, title, author, page_count):
        """Initialize print book attributes.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class that manages a collection of books using composition."""
    
    def __init__(self):
        """Initialize library with an empty book collection."""
        self.books = []
    
    def add_book(self, book):
        """Add a book to the library.
        
        Args:
            book (Book): An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)