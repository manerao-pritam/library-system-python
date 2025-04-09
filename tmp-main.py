# from library import Library
# from book import Book
# from ebook import EBook
# from member import Member
#
# if __name__ == '__main__':
#     lib = Library()
#     book1 = Book("Python 101", "Jane Doe")
#     ebook1 = EBook("Python E-Book", "John Smith", 5)
#     member1 = Member("M001", "Alice")
#
#     lib.add_item(book1)
#     lib.add_item(ebook1)
#     lib.add_member(member1)
#
#     lib.display_available()
#     member1.borrow_item(lib, "Python 101")
#     lib.display_available()
#     member1.return_item(lib, "Python 101")
#     lib.display_available()
#     member1.borrow_item(lib, "Python E-Book")
#     lib.display_available()
#
#     print("\nBorrowing history for Alice:")
#     for record in lib.get_borrowing_history("M001"):
#         print(record)
#     ebook1.check_out()
#
#     '''
#     lib = Library()
#     book1 = Book("Python 101", "Jane Doe")
#     book2 = Book("Python 102", "John Smith")
#
#     lib.add_book(book1)
#     lib.add_book(book2)
#     lib.display_available()
#
#     try:
#         book1.check_out()
#         lib.display_available()
#         book1.check_out()  # Should raise ValueError
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     book1.return_item()
#     lib.display_available()
#
#     found = lib.find_book("Python 101")
#     print(f"Found: {found}")
#     print(f"Not found: {lib.find_book('Python 103')}")
#     '''