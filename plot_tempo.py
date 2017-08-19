# Plot tempo using existing output.h5
from tables import *
import numpy as np
import pylab as P
import matplotlib.pyplot as plt

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

for table in h5file.root.trackinfo:
    tempo = np.array([])

    for track in table:
        tempo = np.append(tempo, track['tempo'])

    tempo = tempo.astype(float)
    p = P.figure()
    bp = P.boxplot(tempo)

    p.suptitle('Tempo Distribution for ' + table.name, fontsize=20)
    P.ylabel('Tempo Score')
    P.ylim([25, 225])

    for i in range(tempo.size):
        y = tempo
        x = np.random.normal(1 + i, 0.04, size=tempo.size)
        P.plot(x, y, 'ro', alpha=0.2)

P.show()
