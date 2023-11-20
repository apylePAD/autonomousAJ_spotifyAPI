# AutonomousAJ's Spotify API Project

## Description
This project provides an interface to interact with the Spotify API, allowing users to search for artists, albums, tracks, and more. It's designed for easy use and flexibility, tailored for those interested in exploring Spotify's vast music database programmatically.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- You have a Spotify account. If not, you can create one at [Spotify](https://www.spotify.com/).

## Obtaining Spotify Credentials
To use this project, you'll need to obtain credentials from Spotify:

1. Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create a new application.
3. Once your application is created, you'll receive a `Client ID` and `Client Secret`.
4. Add these credentials to a `.env` file in your project's root directory as follows:
    ```
    SPOTIFY_CLIENT_ID=your_client_id
    SPOTIFY_CLIENT_SECRET=your_client_secret
    ```
    Replace `your_client_id` and `your_client_secret` with the actual credentials.
    

## Installation
1. Clone the repository: git clone https://github.com/apylePAD/autonomousAJ_spotifyAPI.git
2. Navigate to the project directory: cd autonomousAJ_spotifyAPI
3. Install dependencies: pip install -r requirements.txt

## Usage
Run the main script from the command line to interact with different parts of the Spotify API:


Follow the prompts to search for artists, albums, or tracks.

## Features
- Search for artists on Spotify
- Find albums and tracks
- Modular and extendable codebase

## Contributing
Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
Thanks to Spotify and for providing the API and documentation that made this project possible.
Thank you as well to the Spotipy Python Library, which is an excellent wrapper that makes it very easy to interact and extract data from Spotify's API
