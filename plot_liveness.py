# Plot valence using existing output.h5
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
    liveness = np.array([])

    for track in table:
        liveness = np.append(liveness, track['liveness'])

    liveness = liveness.astype(float)
    p = P.figure()
    bp = P.boxplot(liveness)

    p.suptitle('Acousticness Distribution for ' + table.name, fontsize=20)
    P.ylabel('Acousticness Score')
    P.ylim([0, 1])

    for i in range(liveness.size):
        y = liveness
        x = np.random.normal(1 + i, 0.04, size=liveness.size)
        P.plot(x, y, 'ro', alpha=0.2)

P.show()
