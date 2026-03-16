class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = [] # these a list called "songs"
        self.artist
        
    def add_song(self, song):
        self.songs.append(song)
        print(f"Song {song} is added")
        
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print("song is removed")
            
    def show_song(self):
        print(f"Playlist {self.name}")
        print(f"- {self.artist}")
        for song in self.songs:
            print(f" - {song}")
        
my_playlist = Playlist("Funk")
my_playlist.add_song("Semparo")
my_playlist.add_song("Aura")

my_playlist.show_song()

my_playlist.remove_song("Semparo")
my_playlist.show_song()

