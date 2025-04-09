import pytest

from .member import Member
from .library import Library
from .book import Book
from .ebook import EBook
from .magazine import Magazine

def test_borrow_and_return():
    lib = Library()
    member = Member("M001", "Alice")
    book = Book("Python 101", "Jane Doe")
    lib.add_item(book)
    lib.add_member(member)

    # Borrow
    member.borrow_item(lib, "Python 101")
    assert not book.available
    assert book in member.borrowed_items
    assert len(lib.get_borrowing_history("M001")) == 1

    # Return
    member.return_item(lib, "Python 101")
    assert book.available
    assert book not in member.borrowed_items
    assert len(lib.get_borrowing_history("M001")) == 1  # Fixed: Only 1 record (updated)

def test_max_borrows_limit():
    lib = Library()
    member = Member("M002", "Bob", max_borrows=2)
    books = [Book(f"Book {i}", "Author") for i in range(3)]
    for book in books:
        lib.add_item(book)
    lib.add_member(member)

    # Borrow up to limit
    member.borrow_item(lib, "Book 0")
    member.borrow_item(lib, "Book 1")
    with pytest.raises(ValueError, match="'Bob' has reached the borrowing limit of 2"):
        member.borrow_item(lib, "Book 2")

def test_ebook_download():
    lib = Library()
    member = Member("M003", "Charlie")
    ebook = EBook("Python E-Book", "John Smith", 5)
    lib.add_item(ebook)
    lib.add_member(member)

    with pytest.raises(ValueError, match=r"'Charlie' has not borrowed 'python e-book'"):
        member.return_item(lib, "Python E-Book")  # Not borrowed yet
    member.borrow_item(lib, "Python E-Book")
    assert not ebook.available

def test_clear_history():
    lib = Library()
    member = Member("M004", "Dave")
    book = Book("Test Book", "Test Author")
    lib.add_item(book)
    lib.add_member(member)

    member.borrow_item(lib, "Test Book")
    member.return_item(lib, "Test Book")
    assert len(lib.get_borrowing_history("M004")) == 1
    lib.clear_history()
    assert len(lib.get_borrowing_history("M004")) == 0

def test_magazine_no_checkout():
    lib = Library()
    member = Member("M005", "Eve")
    mag = Magazine("Tech Weekly", 42)
    lib.add_item(mag)
    lib.add_member(member)

    with pytest.raises(ValueError, match="Magazines like 'Tech Weekly' can't be checked out"):
        member.borrow_item(lib, "Tech Weekly")

def test_borrowing_queue():
    lib = Library()
    member1 = Member("M001", "Alice")
    member2 = Member("M002", "Bob")
    book = Book("Popular Book", "Author")
    lib.add_item(book)
    lib.add_member(member1)
    lib.add_member(member2)

    # Member 1 borrows the book
    member1.borrow_item(lib, "Popular Book")
    assert not book.available

    # Member 2 tries to borrow and gets queued
    member2.borrow_item(lib, "Popular Book")
    queue = lib.get_queue_for_item("Popular Book")
    assert not queue.is_empty()
    assert queue.peek() == "M002"

    # Member 1 returns the book, Member 2 should automatically borrow it
    member1.return_item(lib, "Popular Book")
    assert book in member2.borrowed_items
    assert queue.is_empty()

def test_undo_redo_borrow_return():
    lib = Library()
    member = Member("M006", "Frank")
    book = Book("Python 101", "Jane Doe")
    lib.add_item(book)
    lib.add_member(member)

    # Borrow
    member.borrow_item(lib, "Python 101")
    assert not book.available
    assert book in member.borrowed_items

    # Undo borrow
    member.undo(lib)
    assert book.available
    assert book not in member.borrowed_items

    # Redo borrow
    member.redo(lib)
    assert not book.available
    assert book in member.borrowed_items

def test_undo_redo_queue_request():
    lib = Library()
    member1 = Member("M007", "Grace")
    member2 = Member("M008", "Henry")
    book = Book("Popular Book", "Author")
    lib.add_item(book)
    lib.add_member(member1)
    lib.add_member(member2)

    # Member 1 borrows
    member1.borrow_item(lib, "Popular Book")
    assert not book.available

    # Member 2 requests (queues)
    member2.borrow_item(lib, "Popular Book")
    queue = lib.get_queue_for_item("Popular Book")
    assert queue.peek() == "M008"

    # Undo the request
    member2.undo(lib)
    assert queue.is_empty()

    # Redo the request
    member2.redo(lib)
    assert queue.peek() == "M008"