class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        check_genre = Song.genres.count(genre)
        if (check_genre == 0):
            Song.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls, artist):
        check_artist = Song.artists.count(artist)
        if (check_artist == 0):
            Song.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        if (Song.genre_count.get(genre) == None):
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if (Song.artist_count.get(artist) == None):
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist]  += 1

