import sqlite3
from mutagen.mp3 import MP3
from mutagen.aac import AAC
from mutagen.wavpack import WavPack


class Song:
    def __init__(self, db_file):
        self.db_file = db_file

    def modify_tags(self, song_id, new_title=None, new_artist=None, new_album=None):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        if new_title:
            c.execute("UPDATE song SET name=? WHERE id=?", (new_title, song_id))
        if new_artist:
            c.execute("UPDATE song SET artist=? WHERE id=?", (new_artist, song_id))
        if new_album:
            c.execute("UPDATE song SET album=? WHERE id=?", (new_album, song_id))

        conn.commit()
        conn.close()

    def add_song(self, file_path, library_path):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        file_ext = file_path.split(".")[-1].lower()
        if file_ext == 'mp3':
            audio = MP3(file_path)
            title = audio.get('TIT2', 'unknown')
            artist = audio.get('TPE1', 'unknown')
            album = audio.get('TALB', 'unknown')
            duration = int(audio.info.length)

        elif file_ext == 'aac':
            audio = AAC(file_path)
            title = audio.get('title', 'unknown')
            artist = audio.get('artist', 'unknown')
            album = audio.get('album', 'unknown')
            duration = int(audio.info.length)

        elif file_ext == 'wav':
            audio = WavPack(file_path)
            title = audio.get('title', 'unknown')
            artist = audio.get('artist', 'unknown')
            album = audio.get('album', 'unknown')
            duration = int(audio.info.length)

        library_id = self._get_or_create_library(c, library_path)

        c.execute("INSERT INTO song (name, duration, library_id, artist, album) VALUES (?, ?, ?, ?, ?)",
                  (title, duration, library_id, artist, album))

        conn.commit()
        conn.close()

    def delete_song(self, song_id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        c.execute("DELETE FROM song WHERE id=?", (song_id,))

        conn.commit()
        conn.close()

    def _get_or_create_library(self, cursor, library_path):
        cursor.execute("SELECT id FROM library WHERE name=?", (library_path,))
        row = cursor.fetchone()

        if row:
            return row[0]
        else:
            cursor.execute("INSERT INTO library (name) VALUES (?)", (library_path,))
            return cursor.lastrowid
