# Analyze existing output.h5
from tables import *
import numpy as np


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

h5file = open_file('output.h5', mode='r', title='Spotify Tracks')

danceability = np.array([])
acousticness = np.array([])
energy = np.array([])
valence = np.array([])
tempo = np.array([])

for table in h5file.root.trackinfo:
    for track in table:
        danceability = np.append(danceability, track['danceability'])
        acousticness = np.append(acousticness, track['acousticness'])
        energy = np.append(energy, track['energy'])
        valence = np.append(valence, track['valence'])
        tempo = np.append(tempo, track['tempo'])

    print('Average values for ' + table.name + ':')
    print('    Valence:')
    print('        Mean: ' + str(np.mean(valence)))
    print('        Median: ' + str(np.median(valence)))
    print('        Standard Deviation: ' + str(np.std(valence)))
    print('    Danceability:')
    print('        Mean: ' + str(np.mean(danceability)))
    print('        Median: ' + str(np.median(danceability)))
    print('        Standard Deviation: ' + str(np.std(danceability)))
    print('    Acousticness:')
    print('        Mean: ' + str(np.mean(acousticness)))
    print('        Median: ' + str(np.median(acousticness)))
    print('        Standard Deviation: ' + str(np.std(acousticness)))
    print('    Energy:')
    print('        Mean: ' + str(np.mean(energy)))
    print('        Median: ' + str(np.median(energy)))
    print('        Standard Deviation: ' + str(np.std(energy)))
    print('    Tempo:')
    print('        Mean: ' + str(np.mean(tempo)))
    print('        Median: ' + str(np.median(tempo)))
    print('        Standard Deviation: ' + str(np.std(tempo)))
    print()

h5file.close()
