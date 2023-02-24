import sqlite3
import mutagen


class Album:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    # def __del__(self):
    #     self.conn.close()

    def add_album(self, title, artist_name):
        self.cur.execute("SELECT id FROM artist WHERE name = ?", (artist_name,))
        artist_id = self.cur.fetchone()
        if not artist_id:
            self.cur.execute("INSERT INTO artist (name) VALUES (?)", (artist_name,))
            artist_id = self.cur.lastrowid
        else:
            artist_id = artist_id[0]
        self.cur.execute("INSERT INTO album (title, artist_id) VALUES (?, ?, ?)", (title, artist_id))
        self.conn.commit()

    def delete_album(self, album_id):
        self.cur.execute("DELETE FROM album WHERE id = ?", (album_id,))
        self.conn.commit()

    def modify_tag(self, album_id, field, value):
        self.cur.execute("SELECT filename FROM library WHERE album_id = ?", (   album_id,))
        filenames = self.cur.fetchall()
        for filename in filenames:
            try:
                audio = mutagen.File(filename[0])
                if audio:
                    audio[field] = value
                    audio.save()
            except Exception as e:
                print(f"Error modifying tag for {filename[0]}: {e}")

    def show(self, album_id):
        self.cur.execute(
            "SELECT album.title, artist.name FROM album JOIN artist ON album.artist_id = artist.id WHERE album.id = ?",
            (album_id,))
        row = self.cur.fetchone()
        if row:
            print(f"Album: {row[0]}")
            print(f"Artist: {row[1]}")
            self.cur.execute("SELECT title, artist, duration, genre FROM library WHERE album_id = ?", (album_id,))
            rows = self.cur.fetchall()
            for row in rows:
                print(row)
