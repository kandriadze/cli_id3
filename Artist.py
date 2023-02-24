import sqlite3
import mutagen


class Artist:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def add_artist(self, name):
        self.cur.execute("INSERT INTO artist (name) VALUES (?)", (name,))
        self.conn.commit()

    def delete_artist(self, artist_id):
        self.cur.execute("DELETE FROM artist WHERE id = ?", (artist_id,))
        self.conn.commit()

    def modify_tag(self, artist_id, field, value):
        self.cur.execute("SELECT filename FROM library WHERE artist_id = ?", (artist_id,))
        filenames = self.cur.fetchall()
        for filename in filenames:
            try:
                audio = mutagen.File(filename[0])
                if audio:
                    audio[field] = value
                    audio.save()
            except Exception as e:
                print(f"Error modifying tag for {filename[0]}: {e}")

    def show(self):
        self.cur.execute("SELECT name FROM artist")
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0])
