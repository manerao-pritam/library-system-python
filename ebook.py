from .book import Book

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)

        if file_size <= 0:
            raise ValueError("File size must be positive")
        self.file_size = file_size

    def check_out(self):
        super().check_out()
        print("Downloading...")

    def __str__(self):
        return (f"EBook(Title={self.title}, "
                f"Author={self.author}, "
                f"Available={self.available}, "
                f"FileSize={self.file_size}MB)")