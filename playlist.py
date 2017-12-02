#! /usr/bin/env python3
# encoding: utf-8

class Playlist(object):
    '''
    A class that represents a playlist to return
    '''
    def __init__(self):
        self.name = 'Chirpify playlist'
        self.description = ''
        self.tracks = []

    def add_track(self, track):
        '''
        Adds a track to the current playlist
        '''
        self.tracks.append(track)
        