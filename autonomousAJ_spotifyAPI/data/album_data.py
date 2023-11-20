# autonomousAJ_spotifyAPI/data/album_data.py
import pandas as pd
from autonomousAJ_spotifyAPI.api.albums import Albums
from autonomousAJ_spotifyAPI.config import global_config

class Album_Data:
    def __init__(self, album_name):
        self.album_name = album_name
        self.spotify_albums = Albums()

    def get_and_process_album_data(self):
        album_data = self.spotify_albums.search_album(self.album_name)
        
        df_albums = pd.json_normalize(album_data['albums']['items'])
        self.save_album_data(df_albums)

    def save_album_data(self, df_albums):
        df_albums.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/album_data/album_{self.album_name}.csv", index=False)
        print(df_albums)

