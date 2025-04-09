from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def check_out(self) -> None: ...

    @abstractmethod
    def return_item(self) -> None: ...

    @property
    def available(self) -> bool:
        return self._available

    @available.setter
    def available(self, value: bool) -> None:
        self._available = value