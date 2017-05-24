from config import spotify, username, SPOTIPY_REDIRECT_URI, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
from spotipy import util

scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI)
playlists = spotify.user_playlist_create(username, 'My Top Last.fm tracks')
print(playlists)
