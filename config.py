import pylast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# You have to have your own unique two values for Last.fm keys
# Obtain yours from http://www.last.fm/api/account/create for Last.fm
lastfm_public_key = ""
lastfm_secret_key = ""
# This is your last.fm password and stuff
lastfm_username = "h313"
lastfm_password = ""
# This is the username you're trying to look at info about
target = "h313"
# Uncomment one of these to get stats on the top songs
time_period = 'PERIOD_OVERALL'
# time_period = 'PERIOD_12MONTHS'
# time_period = 'PERIOD_6MONTHS'
# time_period = 'PERIOD_3MONTHS'

SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

network = pylast.LastFMNetwork(api_key=lastfm_public_key, api_secret=lastfm_secret_key,
                               username=lastfm_username, password_hash=pylast.md5(lastfm_password))
