-- table
-- id : SERIAL
-- title: text
-- release_year: int
-- artist_id: int
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

INSERT INTO albums (title, release_year, artist_id) VALUES ('Invisible Cities', 2005, 1);
INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');