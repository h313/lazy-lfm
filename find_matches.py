# Finds matches between 2 users using the h5 file

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

track_names = []
usernames = []

for table in h5file.root.trackinfo:
    track_names.append([])
    usernames.append(table.name)
    for track in table:
        track_names[len(track_names) - 1].append(track['song'])

for i in range(len(track_names)):
    for it in range(len(track_names)):
        if i is not it:
            similar = list(set(track_names[i]).intersection(track_names[it]))
            print(usernames[i] + " and " + usernames[it] + " have " + str(len(similar)) + " top tracks in common.")


h5file.close()
