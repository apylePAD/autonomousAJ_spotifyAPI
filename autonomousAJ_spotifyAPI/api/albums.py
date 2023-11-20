# autonomousAJ_spotifyAPI/api/albums.py
from .base import Spotify_API_Base

class Albums(Spotify_API_Base):
    def search_album(self, album_name):
        sp = self.get_spotify_client()
        return sp.search(q=f'album:{album_name}', type='album')
