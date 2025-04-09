from .library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title: str, issue_number: int):
        self.title = title
        self.issue_number = issue_number
        self._available = True

    """
    Getter/Setter
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
    def issue_number(self) -> int:
        return self._issue_number

    @issue_number.setter
    def issue_number(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Issue number must be an integer")
        self._issue_number = value

    """
    Methods 
    """
    def check_out(self) -> None:
        raise ValueError(f"Magazines like '{self.title}' can't be checked out")

    def return_item(self) -> None:
        print(f"'{self.title}' is always in-library")

    def __str__(self):
        return f"Magazine(Title={self.title}, Issue Number={self.issue_number}, Available={self.available})"