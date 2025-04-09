from typing import Optional, List, Dict
from .borrow_record import BorrowRecord
from .member import Member
from .library_item import LibraryItem
from .queue import Queue

class Library:
    def __init__(self):
        self.items: Dict[str, LibraryItem] = {}
        self._history: List[BorrowRecord] = []
        self.members: Dict[str, Member] = {}

        # Queue for books that are unavailable
        self.borrowing_queues: Dict[str, Queue] = {}   # Title -> queue of memberIds

    def add_item(self, item: LibraryItem) -> None:
        key = item.title.lower()
        if key in self.items:
            raise ValueError(f'Item {item.title} already exists')
        self.items[key] = item
        self.borrowing_queues[key] = Queue()             # Initialize Queue for this Item

    def find_item(self, title: str) -> Optional[LibraryItem]:
        return self.items.get(title.lower())

    def list_available(self) -> List[LibraryItem]:
        return [item for item in self.items.values() if item.available]

    def display_available(self):
        available = self.list_available()

        if not available: print("No items available")
        else:
            print("Available items:")
            for item in available:
                print(f"    - {item}")

    def add_member(self, member: Member) -> None:
        if member.id in self.members:
            raise ValueError(f"Member with ID '{member.id}' already exists")
        self.members[member.id] = member

    def add_browsing_history(self, borrow_record: BorrowRecord) -> None:
        self._history.append(borrow_record)

    def get_borrowing_history(self, member_id: Member.id) -> List[BorrowRecord]:
        return [record for record in self._history if record.member_id == member_id]

    def clear_history(self) -> None:
        self._history.clear()
        print("Browsing history cleared")

    def get_queue_for_item(self, title: str) -> Queue:
        title = title.lower()
        if title not in self.borrowing_queues:
            raise ValueError(f'No queue found for item {title}')
        return self.borrowing_queues[title]

