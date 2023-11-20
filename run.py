# autonomousAJ_spotifyAPI/run.py
import inquirer
from autonomousAJ_spotifyAPI.data.album_data import Album_Data
from autonomousAJ_spotifyAPI.data.artist_data import Artist_Data
from autonomousAJ_spotifyAPI.data.track_data import Track_Data

def main_menu():
    questions = [
        inquirer.List('choice',
                      message="What type of data would you like to interact with?",
                      choices=['Artists', 'Albums', 'Tracks', 'Exit']),
    ]
    return inquirer.prompt(questions)['choice']

def get_album_input():
    album_name = input("Enter the album's name: ")
    album_processor = Album_Data(album_name)
    album_processor.get_and_process_album_data()

def get_artist_input():
    artist_name = input("Enter the artist's name: ")
    artist_processor = Artist_Data(artist_name)
    artist_processor.get_and_process_artist_data()

def get_track_input():
    track_name = input("Enter the track's name: ")
    track_processor = Track_Data(track_name)
    track_processor.get_and_process_track_data()

def run():
    while True:
        choice = main_menu()
        if choice == 'Artists':
            get_artist_input()
        elif choice == 'Albums':
            get_album_input()
        elif choice == 'Tracks':
            get_track_input()
        elif choice == 'Exit':
            break

if __name__ == '__main__':
    run()