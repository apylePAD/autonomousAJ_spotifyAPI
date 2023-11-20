import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

class Get_Spotify_Client:
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

    def get_spotify_client(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        return sp

spotify_client = Get_Spotify_Client()