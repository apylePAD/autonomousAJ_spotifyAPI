# autonomousAJ_spotifyAPI/api/artists.py
from .base import Spotify_API_Base

class Artists(Spotify_API_Base):
    def search_artist(self, artist_name):
        sp = self.get_spotify_client()
        return sp.search(q=f'artist:{artist_name}', type='artist')
