# autonomousAJ_spotifyAPI/data/track_data.py
import pandas as pd
from autonomousAJ_spotifyAPI.api.tracks import Tracks
from autonomousAJ_spotifyAPI.config import global_config

class Track_Data:
    def __init__(self, track_name):
        self.track_name = track_name
        self.spotify_tracks = Tracks()

    def get_and_process_track_data(self):
        track_data = self.spotify_tracks.search_track(self.track_name)
        
        df_tracks = pd.json_normalize(track_data['tracks']['items'])
        self.save_track_data(df_tracks)

    def save_track_data(self, df_tracks):
        df_tracks.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/track_data/track_{self.track_name}.csv", index=False)
        print(df_tracks)

