import sqlite3

conn = sqlite3.connect('/music.db')

c = conn.cursor()

c.executescript('''
             DROP TABLE IF EXIST library;
             DROP TABLE IF EXIST song;
             DROP TABLE IF EXIST album;
             DROP TABLE IF EXIST artist;
             DROP TABLE IF EXIST playlist;
             DROP TABLE IF EXIST favorites;

             CREATE TABLE library
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL);

             CREATE TABLE song
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                duration INTEGER,
                library_id INTEGER NOT NULL,
                FOREIGN KEY (library_id) REFERENCES library(id));

             CREATE TABLE album
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                artist_id INTEGER NOT NULL,
                library_id INTEGER NOT NULL,
                FOREIGN KEY (artist_id) REFERENCES artist(id),
                FOREIGN KEY (library_id) REFERENCES library(id));

             CREATE TABLE artist
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL);

             CREATE TABLE playlists
                (id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                song_id INTEGER NOT NULL,
                FOREIGN KEY (song_id) REFERENCES song(id));

             CREATE TABLE favorites
                (id INTEGER PRIMARY KEY,
                song_id INTEGER NOT NULL,
                FOREIGN KEY (song_id) REFERENCES song(id));
''')

conn.commit()

conn.close()
