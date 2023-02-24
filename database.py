import sqlite3

conn = sqlite3.connect('music.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE library
               (id INTEGER PRIMARY KEY,
                title TEXT,
                artist_id INTEGER,
                album_id INTEGER,
                duration INTEGER,
                genre TEXT)''')

cur.execute('''CREATE TABLE artist
               (id INTEGER PRIMARY KEY,
                name TEXT)''')

cur.execute('''CREATE TABLE album
               (id INTEGER PRIMARY KEY,
                title TEXT,
                artist_id INTEGER)''')

cur.execute('''CREATE TABLE song
               (id INTEGER PRIMARY KEY,
                title TEXT,
                artist_id INTEGER,
                album_id INTEGER,
                duration INTEGER,
                genre TEXT)''')

cur.execute('''CREATE TABLE playlist
               (id INTEGER PRIMARY KEY,
                name TEXT)''')

cur.execute('''CREATE TABLE favorites
               (id INTEGER PRIMARY KEY,
                song_id INTEGER,
                FOREIGN KEY(song_id) REFERENCES song(id))''')

conn.commit()
conn.close()
