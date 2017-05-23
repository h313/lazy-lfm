import spotipy
import pylast
import hashlib
from config import network

spotify = spotipy.Spotify()

artist = network.get_artist("System of a Down")

print(artist)