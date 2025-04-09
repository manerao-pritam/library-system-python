from typing import Set, Dict, List
from datetime import datetime

from .library_item import LibraryItem
from .borrow_record import BorrowRecord
from .constants import BORROW_ACTION, RETURN_ACTION, REQUEST_ITEM_ACTION, CANCEL_ITEM_REQUEST_ACTION
from .stack import Stack
from .queue import Queue


class Member:
    def __init__(self, id: str, name: str, max_borrows: int = 3):
        self.id = id                                 # to uniquely identify member
        self.name = name
        self.borrowed_items: Set[LibraryItem] = set()       # set of item
        self.max_borrows = max_borrows

        # undo/redo member actions
        self.undo_stk: Stack = Stack()
        self.redo_stk: Stack = Stack()

    """
    Getter/Setter
    """
    @property
    def id(self): return self._id

    @id.setter
    def id(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("ID must be a non-empty string")
        self._id = value

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    """
    Methods
    """
    def borrow_item(self, library: 'Library', title: str) -> None:
        title = title.strip().lower()
        item = library.find_item(title)

        if not item:
            raise ValueError(f'Item {title} not found')

        if item in self.borrowed_items:
            raise ValueError(f"'{self.name}' already borrowed '{title}'")

        if len(self.borrowed_items) >= self.max_borrows:
            raise ValueError(f"'{self.name}' has reached the borrowing limit of {self.max_borrows}")

        if item.available:
            item.check_out()
            self.borrowed_items.add(item)

            # adding browsing history
            library.add_browsing_history(BorrowRecord(self.id, title))

            # add to undo queue
            self.undo_stk.push({"action": BORROW_ACTION, "title": title})
        else:
            self.request_item(library, title)


    def return_item(self, library: 'Library', title: str) -> None:
        title = title.strip().lower()

        item = library.find_item(title)

        if not item:
            raise ValueError(f'Item {title} not found')

        if item not in self.borrowed_items:
            raise ValueError(f"'{self.name}' has not borrowed '{title}'")

        item.return_item()
        self.borrowed_items.remove(item)

        # add to undo queue
        self.undo_stk.push({"action": RETURN_ACTION, "title": title})

        # update exiting record
        for record in library._history:
            if record.member_id == self.id and record.item_title == title and record.is_active():
                record.return_date = datetime.now()
                break

        """
        TODO:
        Queue Processing:
        If the next member in the queue can’t borrow the item (e.g., they’ve reached their max_borrows limit), the current implementation will raise an error and stop. You might want to handle this by continuing to process the queue until a member can borrow the item or the queue is empty. This can be a future enhancement.
        """
        # process the queue
        queue = library.get_queue_for_item(title)
        if not queue.is_empty():
            next_member_id = queue.dequeue()
            next_member = library.members.get(next_member_id)
            if next_member:
                next_member.borrow_item(library, title)
                print(f"'{next_member.name}' (ID: {next_member_id}) borrowed '{title}' from the queue")

    def request_item(self, library: 'Library', title: str) -> None:
        queue = library.get_queue_for_item(title)
        queue.enqueue(self.id)  # add member id in the queue for item title
        print(f"{self.name} added to the queue for '{title}'")

        # add to undo queue
        self.undo_stk.push({"action": REQUEST_ITEM_ACTION, "title": title})

    def cancel_item_request(self, library: 'Library', title: str) -> None:
        title = title.strip().lower()
        queue = library.get_queue_for_item(title)
        # Create a temporary list to rebuild the queue without this member's ID
        temp_queue = Queue()
        found = False
        while not queue.is_empty():
            member_id = queue.dequeue()
            if member_id != self.id:
                temp_queue.enqueue(member_id)
            else:
                found = True
        # Rebuild the queue
        while not temp_queue.is_empty():
            queue.enqueue(temp_queue.dequeue())
        if not found:
            raise ValueError(f"'{self.name}' is not in the queue for '{title}'")
        print(f"'{self.name}' removed from the queue for '{title}'")

    """
    action = {
        "action": RETURN_ACTION,
        "title": title
    }
    """
    def undo(self, library: 'Library') -> None:
        if not self.undo_stk.is_empty():
            action = self.undo_stk.pop()
            action_to_redo = self._perform_action(library, action)
            self.redo_stk.push(action_to_redo)

    def redo(self, library: 'Library') -> None:
        if not self.redo_stk.is_empty():
            action = self.redo_stk.pop()
            action_to_undo = self._perform_action(library, action)
            self.undo_stk.push(action_to_undo)

    def _perform_action(self, library: 'Library', action: Dict[str, str]) -> Dict[str, str]:
        action_type = action.get("action")
        title = action.get("title")

        if not action_type or not title:
            raise ValueError("Invalid action format")

        match action_type:
            case "borrow":
                self.return_item(library, title)
                return {"action": RETURN_ACTION, "title": title}

            case "return":
                self.borrow_item(library, title)
                return {"action": BORROW_ACTION, "title": title}

            case "request_item":
                self.cancel_item_request(library, title)
                return {"action": CANCEL_ITEM_REQUEST_ACTION, "title": title}

            case "cancel_request_item":
                self.request_item(library, title)
                return {"action": REQUEST_ITEM_ACTION, "title": title}

            case _:
                raise ValueError(f'Invalid action {action["action"]}')