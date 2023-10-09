from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from lib.book import Book
from flask import request

# You won't need to nest your routes in app.py in a method like this
def apply_example_routes(app):
    # GET /books
    # Returns a list of books
    # Try it:
    #   ; curl http://localhost:5001/books
    @app.route('/books', methods=['GET'])
    def get_books():
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)
        return "\n".join([
            str(book) for book in repository.all()
        ])


    # GET /books/<id>
    # Returns a single book
    # Try it:
    #   ; curl http://localhost:5001/books/1
    @app.route('/books/<int:id>', methods=['GET'])
    def get_book(id):
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)
        return str(repository.find(id))


    # POST /books
    # Creates a new book
    # Try it:
    #   ; curl -X POST -d "title=Dave&author_name=Caden%20Lovelace" http://localhost:5001/books
    @app.route('/books', methods=['POST'])
    def create_book():
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)
        book = Book(None, request.form['title'], request.form['author_name'])
        book = repository.create(book)
        return "Book added successfully"


    # DELETE /books/<id>
    # Deletes a book
    # Try it:
    #   ; curl -X DELETE http://localhost:5001/books/1
    @app.route('/books/<int:id>', methods=['DELETE'])
    def delete_book(id):
        connection = get_flask_database_connection(app)
        repository = BookRepository(connection)
        repository.delete(id)
        return "Book deleted successfully"
