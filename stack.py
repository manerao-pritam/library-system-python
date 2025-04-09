from typing import Dict

from .constants import BORROW_ACTION, RETURN_ACTION, REQUEST_ITEM_ACTION, CANCEL_ITEM_REQUEST_ACTION

class Stack:
    def __init__(self):
        self.actions = []

    def push(self, action: Dict[str, str]):
        if ("action" not in action
                or action["action"] not in (BORROW_ACTION,
                                            RETURN_ACTION,
                                            REQUEST_ITEM_ACTION,
                                            CANCEL_ITEM_REQUEST_ACTION)):
            raise ValueError(
                f"Action type is not valid. It must be one of: {BORROW_ACTION}, {RETURN_ACTION}, {REQUEST_ITEM_ACTION}, {CANCEL_ITEM_REQUEST_ACTION}")
        self.actions.append(action)

    def pop(self) -> Dict[str, str]:
        if self.is_empty():
            raise IndexError("Popping from an empty stack")
        return self.actions.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peeking an empty stack")
        return self.actions[-1]

    def is_empty(self):
        return not self.actions

    def __len__(self):
        return len(self.actions)

    def __str__(self):
        return f"Stack({self.actions})"