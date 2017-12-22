# Chirpify

Chirpify is a Python library that takes the CHIRP DJ profile setlist and turns it into a Spotify playlist. Just point the CLI at a DJ's profile page on the CHIRP website along with the playlist name and the code will create an entire playlist with every track that DJ has ever played.

### Prerequisites

Python3 (Python2 will require a couple code changes)

[Spotify account](https://www.spotify.com/us/signup/)

[Spotify API Credentials](https://developer.spotify.com/my-applications/#!/)

BeautifulSoup
```
pip3 install beautifulsoup4
```

Spotipy
```
pip3 install spotipy
```

Requests
```
pip3 install requests
```

### Installing

Clone this repository

```
git clone https://github.com/clintmcmahon/chirpify.git
```

Change directory to chirpify

```
cd chirpify
```

Create a local_config.py file and populate with your values. Your file should look like this

```
#!/usr/bin/env python
#encoding: utf-8

SPOTIFY_USERNAME = [your Spotify username]
SPOTIFY_CLIENT_SECRET = [your Spotify API Client Secret]
SPOTIFY_CLIENT_ID = [your Spotify API Client ID]
SPOTIFY_SCOPE = 'playlist-modify-public playlist-modify-private playlist-read-collaborative'
SPOTIFY_REDIRECT_URI = 'http://localhost'
```

Run the code
```
python3 main.py --uri http://chirpradio.org/dj/XXXX --name 'Awesome tunes' --full (optional, leave off for most recent)
```
A browser window will automatically open where you will authenticate with Spotify. After you've given access to your Spotify account the browser will redirect to a http://localhost url. Copy the localhost url and paste it into the command line. You'll only need to do this once, the code will create a cache authentication file on your local machine.

After you've authenticated the program will read the CHIRP profile and either create a new playlist with the given name or append to the playlist if the name already exists.

## Built With

* [Spotify](http://www.spotify.com)
* [Chirp Radio](http://chirpradio.org)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Spotipy](https://github.com/plamere/spotipy)

## Acknowledgments

* Chicago Independent Radio Project - [Help Keep Great Music Commerical Free And Donate Today!](http://chirpradio.org/donations)
