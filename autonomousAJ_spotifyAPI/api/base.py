# autonomousAJ_spotifyAPI/api/base.py
from autonomousAJ_spotifyAPI.auth import spotify_client
import requests

class Spotify_API_Base:
    def get_spotify_client(self):
        return spotify_client.get_spotify_client()

    def handle_api_call(self, api_function, *args, **kwargs):
        try:
            response = api_function(*args, **kwargs)
            response.raise_for_status()  # Raises an HTTPError for bad requests
            return response

        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")

        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")

        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")

        except requests.exceptions.RequestException as err:
            print(f"Other Error: {err}")

        return None
