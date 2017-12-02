#! /usr/bin/env python3
# encoding: utf-8

import sys
import datetime
from spotify import Spotify
from chirpScraper import Scrape
from playlist import Playlist
import json


def main(uri, playlist_name):
    '''
    Main method
    '''

    scrape = Scrape(uri)
    tracks = scrape.get_tracks()
    
    spotify = Spotify()
    playlist = Playlist()
    playlist.tracks = tracks
    playlist.name = playlist_name
    playlist.description = 'Not implemented yet'
    playlist_id = spotify.create_playlist(playlist)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        uri = sys.argv[1]
        if(len(sys.argv) > 2):
            playlist_name = sys.argv[2]
        else:
            playlist_name = 'Chirpify'
    else:
        print ("Whoops, need a playlist uri!")
        print ("usage: python main.py [playlistUri] [playlist name (optional)]")
        sys.exit()

    main(uri, playlist_name)