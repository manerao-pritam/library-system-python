from .library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._available = True

    """
    Getter/Setters
    """
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author must be a non-empty string")
        self._author = value

    """
    Methods
    """
    def check_out(self):
        if not self.available:
            raise ValueError(f"Checkout failed! {self.title} by {self.author} is not available.")

        self.available = False
        print(f"{self.title} by {self.author} checked out")

    def return_item(self):
        if self.available:
           raise ValueError(f"Return failed! {self.title} by {self.author} is already available")

        self.available = True
        print(f"{self.title} by {self.author} returned")

    def __str__(self):
        return f"Book(Title={self.title}, Author={self.author}, Available={self.available})"