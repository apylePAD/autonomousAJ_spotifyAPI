# autonomousAJ_spotifyAPI/run.py
import inquirer
from autonomousAJ_spotifyAPI.data.artist_data import Artist_Data
# Import other data modules as needed

def main_menu():
    questions = [
        inquirer.List('choice',
                      message="What type of data would you like to interact with?",
                      choices=['Artists', 'Albums', 'Tracks', 'Exit']),
    ]
    return inquirer.prompt(questions)['choice']

def get_artist_input():
    artist_name = input("Enter the artist's name: ")
    artist_processor = Artist_Data(artist_name)
    artist_processor.get_and_process_artist_data()

def run():
    while True:
        choice = main_menu()
        if choice == 'Artists':
            get_artist_input()
        # elif choice == 'Albums':
        #     # Implement album functionality
        # elif choice == 'Tracks':
        #     # Implement track functionality
        elif choice == 'Exit':
            break

if __name__ == '__main__':
    run()