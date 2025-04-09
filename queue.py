class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item) -> None:
        """Add an item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the first item in the queue"""
        if self.is_empty():
            raise IndexError("Can't dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the first item in the queue"""
        if self.is_empty():
            raise IndexError("Can't peek an empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise"""
        return len(self.items) == 0

    def __len__(self) -> int:
        """Return the length of items in the queue"""
        return len(self.items)

    def __str__(self):
        return  f'Queue({self.items})'