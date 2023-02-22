from PIL import Image
import main
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3


class Song(main.MusicItem):
    def __init__(self, path):
        super().__init__(path)


def get_tags(self):
    tags = EasyID3(self.path)
    if not tags:
        tags = {'title': 'Unknown', 'artist': 'Unknown', 'album': 'Unknown'}
    return tags


def set_tags(self, title, artist, album):
    tags = EasyID3(self.path)
    tags['title'] = title
    tags['artist'] = artist
    tags['album'] = album
    tags.save()


def get_duration(self):
    audio = MP3(self.path)
    return audio.info.length


def get_artwork(self, album_name):
    if album_name not in self.albums:
        return None
    artwork_path = self.albums[album_name]['artwork_path']
    if artwork_path is None:
        return None
    with open(artwork_path, 'rb') as f:
        return Image.open(f)
