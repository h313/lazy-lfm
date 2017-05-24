from tables import *
from config import network, time_period, spotify, target


class Track(IsDescription):
    song = StringCol(32)
    album = StringCol(32)
    danceability = Float32Col()
    loudness = Float32Col()
    acousticness = Float32Col()
    instrumentalness = Float32Col()
    liveness = Float32Col()
    valence = Float32Col()


h5file = open_file("output.h5", mode="w", title="Spotify Tracks")
group = h5file.create_group(h5file.root, 'trackinfo', 'track information')

table = h5file.create_table(group, target, Track)
track = table.row

top = network.get_user(target).get_top_tracks(time_period)

for i in range(50):
    result = spotify.search(q='track:"' + top[i].item.title + '"artist:"' + top[i].item.artist.name + '"',
                            type='track')

    if len(result['tracks']['items']) is not 0:
        analysis = spotify.audio_features(result['tracks']['items'][0]['uri'])[0]

        track['song'] = result['tracks']['items'][0]['name']
        track['album'] = result['tracks']['items'][0]['album']['name']
        track['danceability'] = analysis['danceability']
        track['loudness'] = analysis['loudness']
        track['acousticness'] = analysis['acousticness']
        track['instrumentalness'] = analysis['instrumentalness']
        track['liveness'] = analysis['liveness']
        track['valence'] = analysis['valence']
        track.append()
        print(result['tracks']['items'][0]['name'] + ' - ' + result['tracks']['items'][0]['album']['name'])
        table.flush()

print(h5file)
h5file.close()
