import sqlite3

conn = sqlite3.connect('music.db')

conn.execute('''CREATE TABLE IF NOT EXISTS music_item (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    artist TEXT,
                    album TEXT,
                )''')

conn.execute('''CREATE TABLE IF NOT EXISTS library (
                    song_id INTEGER PRIMARY KEY,
                    title  TEXT NOT NULL
                )''')

conn.execute('''CREATE TABLE IF NOT EXISTS playlist (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')

conn.execute('''CREATE TABLE IF NOT EXISTS playlist_song (
                    playlist_id INTEGER,
                    song_id INTEGER,
                    PRIMARY KEY (playlist_id, song_id),
                    FOREIGN KEY (playlist_id) REFERENCES playlist(id),
                    FOREIGN KEY (song_id) REFERENCES music_item(id)
                )''')

conn.execute('''CREATE TABLE IF NOT EXISTS album (
                    album_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')

conn.execute('''CREATE TABLE IF NOT EXISTS album_song (
                    album_id,
                    song_id INTEGER,
                    PRIMARY KEY (album_id, song_id),
                    FOREIGN KEY (album_id) REFERENCES album(id),
                    FOREIGN KEY (song_id) REFERENCES music_item(id)
                )''')

conn.execute('''CREATE TABLE IF NOT EXISTS artist (
                    id INTEGER PRIMARY KEY,
                    artist TEXT NOT NULL
                )''')

conn.execute('''CREATE TABLE IF NOT EXISTS favorites (
                    id INTEGER PRIMARY KEY,
                    song_id integer
                )''')
conn.commit()
conn.close()
