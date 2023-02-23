import os
from abc import ABC, abstractmethod
import sqlite3
from mutagen.aac import AAC
from mutagen.wavpack import WavPack
from mutagen.mp3 import MP3


class MusicItem(ABC):
    def __init__(self, path):
        self.path = path


@abstractmethod
def get_tags(self):
    pass


@abstractmethod
def set_tags(self, title, artist, album):
    pass


@abstractmethod
def modify_tag(self):
    pass


@abstractmethod
def get_duration(self):
    pass


@abstractmethod
def get_artwork(self):
    pass


# @abstractmethod
# def show(self):
#     pass


class Library:
    def __init__(self, db_file):
        self.db_file = db_file

    def scan_directory(self, directory):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file)[-1].lower()

                if file_ext in ('.mp3', '.aac', '.wav'):
                    try:
                        if file_ext == '.mp3':
                            audio = MP3(file_path)
                            title = audio.get('TIT2', 'unknown')
                            artist = audio.get('TPE1', 'unknown')
                            album = audio.get('TALB', 'unknown')
                            duration = int(audio.info.length)

                        elif file_ext == '.aac':
                            audio = AAC(file_path)
                            title = audio.get('title', 'unknown')
                            artist = audio.get('artist', 'unknown')
                            album = audio.get('album', 'unknown')
                            duration = int(audio.info.length)

                        elif file_ext == '.wav':
                            audio = WavPack(file_path)
                            title = audio.get('title', 'unknown')
                            artist = audio.get('artist', 'unknown')
                            album = audio.get('album', 'unknown')
                            duration = int(audio.info.length)

                        library_id = self._get_or_create_library(c, root)

                        c.execute("INSERT INTO song (name, duration, library_id, artist, album) VALUES (?, ?, ?, ?, ?)",
                                  (title, duration, library_id, artist, album))

                    except Exception as e:
                        print(f"Failed to read tags for {file_path}: {str(e)}")

        conn.commit()
        conn.close()

    def _get_or_create_library(self, cursor, library_path):
        cursor.execute(f"SELECT id FROM library WHERE name='{library_path}'")
        row = cursor.fetchone()

        if row:
            return row[0]
        else:
            cursor.execute(f"INSERT INTO library (name) VALUES (?)", (library_path,))
            return cursor.lastrowid

    def add_directory(self, directory):
        self.scan_directory(directory)

    def delete_song(self, song_id):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        c.execute("DELETE FROM song WHERE id=?", (song_id,))

        conn.commit()
        conn.close()
