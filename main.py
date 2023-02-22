import os
import glob
from abc import ABC, abstractmethod
import Song


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


class MusicLibrary:
    def __init__(self, directories=[]):
        self.songs = []
        self.albums = {}
        self.artists = {}
        self.directories = directories()


def scan_directories(self):
    for directory in self.directories:
        for file in glob.glob(os.path.join(directory, ('*.mp3', '*.wav', '*.acc '))):
            song = Song(file)
            self.songs.append(song)


def add_to_artists(self, song):
    artist = song.get_tags().get('artist', 'Unknown')
    if artist in self.artists:
        self.artists[artist].append(song)
    else:
        self.artists[artist] = [song]


def show(self):
    print(f"{'Title':<40}{'Artist':<20}{'Album':<30}{'Duration':<10}")
    for song in self.songs:
        print(
            f"{song.get_tags()['title'][0]:<40}{song.get_tags()['artist'][0]:<20}{song.get_tags()['album'][0]:<30}{song.get_duration():<10.2f}")


def add_directory(self, directory):
    self.directories.append(directory)


def remove_directory(self, directory):
    self.directories.remove(directory)

# def play(self):
#     for song in self.songs:
#         print(f"Now playing {song.get_tags()['title'][0]} by {song.get_tags()['artist'][0]}")
