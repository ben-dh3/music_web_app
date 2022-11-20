"""
GET /books
"""
def test_get_books(db_connection, web_client): # Note web_client fixture, see conftest.py
    # We seed our database with the book store seed file
    db_connection.seed("seeds/book_store.sql")

    # We make a GET request to /books
    response = web_client.get("/books")

    # We assert that the response status code is 200
    assert response.status_code == 200

    # We assert that the response data is the same as the string we expect
    assert response.data.decode("utf-8") == "\n".join([
        "Book(1, Invisible Cities, Italo Calvino)",
        "Book(2, The Man Who Was Thursday, GK Chesterton)",
        "Book(3, Bluets, Maggie Nelson)",
        "Book(4, No Place on Earth, Christa Wolf)",
        "Book(5, Nevada, Imogen Binnie)"
    ])

"""
GET /books/<id>
"""
def test_get_book(db_connection, web_client):
    db_connection.seed("seeds/book_store.sql")

    response = web_client.get("/books/1")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "" \
        "Book(1, Invisible Cities, Italo Calvino)"

"""
POST /books
"""
def test_create_book(db_connection, web_client):
    db_connection.seed("seeds/book_store.sql")

    response = web_client.post("/books", data={
        "title": "The Great Gatsby",
        "author_name": "F. Scott Fitzgerald"
    })

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book added successfully"

    response = web_client.get("/books")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Book(1, Invisible Cities, Italo Calvino)\n" +
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" +
        "Book(3, Bluets, Maggie Nelson)\n" +
        "Book(4, No Place on Earth, Christa Wolf)\n" +
        "Book(5, Nevada, Imogen Binnie)\n" +
        "Book(6, The Great Gatsby, F. Scott Fitzgerald)"
    ])

"""
DELETE /books/<id>
"""
def test_delete_book(db_connection, web_client):
    db_connection.seed("seeds/book_store.sql")

    response = web_client.delete("/books/1")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Book deleted successfully"

    response = web_client.get("/books")

    assert response.status_code == 200
    assert response.data.decode("utf-8") == "\n".join([
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" +
        "Book(3, Bluets, Maggie Nelson)\n" +
        "Book(4, No Place on Earth, Christa Wolf)\n" +
        "Book(5, Nevada, Imogen Binnie)"
    ])

