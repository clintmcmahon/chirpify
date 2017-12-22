#! /usr/bin/env python3
# encoding: utf-8

import sys
import datetime
from spotify import Spotify
from chirpScraper import Scrape
from playlist import Playlist
import json
import argparse

def main(uri, playlist_name, most_recent):
    '''
    Main method
    '''

    scrape = Scrape(uri, most_recent)
    tracks = scrape.get_tracks()
    
    spotify = Spotify()
    playlist = Playlist()
    playlist.tracks = tracks
    playlist.name = playlist_name
    playlist.description = 'Not implemented yet'
    playlist_id = spotify.create_playlist(playlist)

if __name__ == '__main__':
    most_recent = True
    uri = ''
    playlist_name = 'Chirpify'

    # initiate the parser
    parser = argparse.ArgumentParser()  
    parser.add_argument('-U', '--uri', help='set the dj profile url')
    parser.add_argument('-N', '--name', help='set the name of the playlist')
    parser.add_argument('-F', '--full', help='download the full dj playlist archive', action='store_true')

    # read arguments from the command line
    args = parser.parse_args()

    if args.uri:
        uri = args.uri
    else:
        print ('Whoops, need a playlist uri!')
        print ('usage: python3 main.py --uri http://chirpradio.org/dj/XXXX')
        sys.exit()
    if args.name:
        playlist_name = args.name
    if args.full:  
        most_recent = False

    main(uri, playlist_name, most_recent)