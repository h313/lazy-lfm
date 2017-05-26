import pylast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# You have to have your own unique two values for Last.fm keys
# Obtain yours from http://www.last.fm/api/account/create for Last.fm
lastfm_public_key = ""
lastfm_secret_key = ""
# You have to have your own unique two values for Spotify API keys
# Obtain yours from https://developer.spotify.com/my-applications/#!/applications/create
SPOTIPY_CLIENT_ID = "
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = ''

# This is your last.fm password and stuff
lastfm_username = ""
lastfm_password = ""
# This is your spotify username
username = ""

# Use the following two configs for create_hdf5.py
# This is the usernames you're trying to look at info about
targets = ["", "", ""]

# Uncomment one of these to get stats on the top songs
time_period = 'PERIOD_OVERALL'
# time_period = 'PERIOD_12MONTHS'
# time_period = 'PERIOD_6MONTHS'
# time_period = 'PERIOD_3MONTHS'

# Use the following if you are using create_playlist.py, which requires an output.h5

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

network = pylast.LastFMNetwork(api_key=lastfm_public_key, api_secret=lastfm_secret_key,
                               username=lastfm_username, password_hash=pylast.md5(lastfm_password))
