class Album:
    def __init__(self, album):
        self.album = album

    def add_album(self, song):
        album = song.get_tags().get('album', 'Unknown')
        if album in self.albums:
            self.albums[album].append(song)
        else:
            self.albums[album] = [song]

    def remove_album(self, song):
        pass

    def get_artwork(self):
        pass

    def modify_tag(self, song):
        pass
