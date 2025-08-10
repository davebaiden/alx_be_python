class Book:
    """A simple Book class demonstrating Python magic methods."""

    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Called when the object is about to be destroyed.

        Prints a simple deletion message including the book title.
        """
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Informal string representation for end-users.

        Example: "1984 by George Orwell, published in 1949"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Official representation that can be used to recreate the object.

        Example: "Book('1984', 'George Orwell', 1949)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
