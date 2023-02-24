import os
import mutagen
import sqlite3


class Library:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def scan_directory(self, dir_path):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(('.mp3', '.wav', '.aac')):
                    full_path = os.path.join(root, file)
                    try:
                        audio = mutagen.File(full_path)
                        if audio:
                            title = audio.get('title', ['unknown'])[0]
                            artist = audio.get('artist', ['unknown'])[0]
                            album = audio.get('album', ['unknown'])[0]
                            duration = int(audio.info.length)
                            genre = audio.get('genre', ['unknown'])[0]
                            filename = os.path.basename(full_path)
                            self.cur.execute(
                                "INSERT INTO library (title, artist, album, duration, genre, filename) VALUES (?, ?, ?, ?, ?, ?)",
                                (title, artist, album, duration, genre, filename))
                            self.conn.commit()
                    except Exception as e:
                        print(f"Error processing file {full_path}: {e}")

    def add_directory(self, dir_path):
        self.scan_directory(dir_path)

    def delete_directory(self, dir_path):
        self.cur.execute("DELETE FROM library WHERE filename LIKE ?", (f"%{dir_path}%",))
        self.conn.commit()

    def display_library(self):
        self.cur.execute("SELECT * FROM library")
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
