# autonomousAJ_spotifyAPI/api/tracks.py
from .base import Spotify_API_Base

class Tracks(Spotify_API_Base):
    def search_track(self, track_name):
        sp = self.get_spotify_client()
        return sp.search(q=f'track:{track_name}', type='track')
