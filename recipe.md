exercise: test driving route with databse

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

table
id : SERIAL
title: text
release_year: int
artist_id: int

# plain route recipe

POST /albums
title: string
release_year: int
artist_id: int

POST /albums

Parameters:
title=Voyage
release_year=2022
artist_id=2

Expected response (200 OK):
"""
(No content)
"""
assert that new album is present in list of records returned by GET /albums

<!--            -->


challenge: test driving route with database

<!-- GET artists -->

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

<!-- Post artists -->

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing