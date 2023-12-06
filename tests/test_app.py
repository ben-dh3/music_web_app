from lib.album_repository import *
from lib.album import *
from lib.artist_repository import *
from lib.artist import *
# Tests for your routes go here

# List all the albums
# Request: GET /albums
# Response: list of albums

"""
When we call list_albums
We get a list of album objects reflecting the seed data.
"""
def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Invisible Cities, 2005, 1)"
    
# title=Voyage
# release_year=2022
# artist_id=2

# Create a new albums
# Request: POST /albums
#   With body parameters: "title=Voyage&release_year=2022&artist_id=2"
# Response: None (just creates the resource on the server)

def test_post_albums(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.post('/albums', data={
        'title': 'Voyage',
        'release_year': 2022,
        'artist_id': 2
    })
    assert response.status_code == 200
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
    "Album(1, Invisible Cities, 2005, 1)\n" \
    "Album(2, Voyage, 2022, 2)"

def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        'Pixies'
    
def test_post_artists(web_client, db_connection):
    db_connection.seed('seeds/music_web_app.sql')
    response = web_client.post('/artists', data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert response.status_code == 200
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
    "Pixies\n" \
    "Wild nothing"


# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
