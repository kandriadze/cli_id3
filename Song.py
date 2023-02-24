import sqlite3
import mutagen


class Song:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()

    def add_song(self):
        pass

    def delete_song(self):
        pass

    def modify_tags(self):
        pass

    def show(self):
        pass









