# Pulls top 50 Last.fm songs and puts that data into output.h5
from tables import *
from config import network, time_period, spotify, targets


class Track(IsDescription):
    song = StringCol(128)
    album = StringCol(128)
    danceability = Float32Col()
    loudness = Float32Col()
    acousticness = Float32Col()
    instrumentalness = Float32Col()
    liveness = Float32Col()
    energy = Float32Col()
    speechiness = Float32Col()
    valence = Float32Col()
    tempo = Float32Col()
    key = Int32Col()
    mode = StringCol(5)

h5file = open_file('output.h5', mode='w', title='Spotify Tracks')
group = h5file.create_group(h5file.root, 'trackinfo', 'track information')

for target in targets:
    print('creating new table for ' + target + '...')
    table = h5file.create_table(group, target, Track)
    track = table.row

    print('getting top songs for ' + target + '...')
    top = network.get_user(target).get_top_tracks(time_period)

    print('getting songs...')
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
            track['speechiness'] = analysis['speechiness']
            track['tempo'] = analysis['tempo']
            track['energy'] = analysis['energy']
            track['key'] = analysis['key']
            track['mode'] = 'minor' if analysis['mode'] is 0 else 'major'
            track.append()
            print(result['tracks']['items'][0]['name'] + ' - ' + result['tracks']['items'][0]['album']['name'])
            table.flush()

    print('finished!')

h5file.close()
