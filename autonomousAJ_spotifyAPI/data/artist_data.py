# autonomousAJ_spotifyAPI/data/artist_data.py
import pandas as pd
from autonomousAJ_spotifyAPI.api.artists import Artists
from autonomousAJ_spotifyAPI.config import global_config

class Artist_Data:
    def __init__(self, artist_name):
        self.artist_name = artist_name
        self.spotify_artists = Artists()

    def get_and_process_artist_data(self):
        artist_data = self.spotify_artists.search_artist(self.artist_name)
        
        df_artists = pd.json_normalize(artist_data['artists']['items'])
        self.save_artist_data(df_artists)

    def save_artist_data(self, df_artists):
        df_artists.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/artist_data/artists_{self.artist_name}.csv", index=False)
        print(df_artists)

