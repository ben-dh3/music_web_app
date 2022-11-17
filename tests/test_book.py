from lib.book import Book

"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book = Book(1, "Test Title", "Test Author")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author"

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "Test Title", "Test Author")
    assert str(book) == "Book(1, Test Title, Test Author)"
    # Try commenting out the `__repr__` method in lib/book.py
    # And see what happens when you run this test again.

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test Title", "Test Author")
    book2 = Book(1, "Test Title", "Test Author")
    assert book1 == book2
    # Try commenting out the `__eq__` method in lib/book.py
    # And see what happens when you run this test again.
