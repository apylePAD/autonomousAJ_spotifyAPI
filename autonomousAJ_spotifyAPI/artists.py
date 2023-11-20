# autonomousAJ_spotifyAPI/artists.py
import json
import pandas as pd
from autonomousAJ_spotifyAPI.config import global_config
from autonomousAJ_spotifyAPI.auth import spotify_client

class Get_Artist_Data:
    def __init__(self, artist):
        self.artist = artist

    def get_artist_data(self):

        sp = spotify_client.get_spotify_client()
        results = sp.search(q=f'artist:{self.artist}', type='artist')

        self.artist_data = {
            "artists": results['artists']['items']
        }

    def write_artist_data(self):
        artists = pd.DataFrame(self.artist_data)
        df_artists = pd.json_normalize(artists['artists'])
        df_artists.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/artists.csv", index=False)
        print(df_artists)


artist = Get_Artist_Data('Beatles')
artist.get_artist_data()
artist.write_artist_data()