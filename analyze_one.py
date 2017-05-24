from config import spotify
import json

TRACK = 'Everglow'
ARTIST = 'Coldplay'

result = spotify.search(q='track:"' + TRACK + '"artist:"' + ARTIST + '"', type='track')

if len(result['tracks']['items']) is not 0:
    analysis = spotify.audio_features(result['tracks']['items'][0]['uri'])[0]
    print('Name: ' + result['tracks']['items'][0]['name'])
    print('Album: ' + result['tracks']['items'][0]['album']['name'])
    print('Danceability: ' + str(analysis['danceability']))
    print('Loudness: ' + str(analysis['loudness']))
    print('Acousticness: ' + str(analysis['acousticness']))
    print('Instrumentalness: ' + str(analysis['instrumentalness']))
    print('Liveliness: ' + str(analysis['liveness']))
    print('Valence: ' + str(analysis['valence']))
    print('Speechiness: ' + str(analysis['speechiness']))
    print('Tempo: ' + str(analysis['tempo']))
    print('Energy: ' + str(analysis['energy']))
    print('Key: ' + str(analysis['key']))
    print('Mode' + 'minor' if analysis['mode'] is 0 else 'major')
