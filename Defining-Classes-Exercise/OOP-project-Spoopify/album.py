from Library.song import Song
class Album:
    def __init__(self, name, *args,):
        self.name = name
        self.songs = list(args)
        self.published = False


    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.is_single:
            return f"Cannot add {song.name}. It's a single"
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."


    def remove_song(self, song_name):
        songs = [p for p in self.songs if p.name == song_name]
        if songs:
            if not self.published:
                self.songs.remove(songs[0])
                return f"Removed song {songs[0].name} from album {self.name}."
            else:
                return "Cannot remove songs. Album is published."
        return "Song is not in the album."


    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."


    def details(self):
        result = f"Album {self.name}\n"
        for songs in self.songs:
            result += "== "+songs.get_info()+"\n"
        return result

