#! /usr/bin/env python3
# encoding: utf-8

import sys
import datetime
from spotify import Spotify
from chirpScraper import Scrape
from playlist import Playlist
import json
import argparse


def worker_b(uri, playlist_name, most_recent):
    '''Creates objects and does the real work
    '''
    scrape = Scrape(uri, most_recent)
    tracks = scrape.get_tracks()
    
    spotify = Spotify()
    playlist = Playlist()
    playlist.tracks = tracks
    playlist.name = playlist_name
    playlist.description = 'Not implemented yet'
    playlist_id = spotify.create_playlist(playlist)

def main():
    '''
    Main method
    '''
    most_recent = True
    uri = ''
    playlist_name = 'Chirpify'

    # initiate the parser
    parser = argparse.ArgumentParser(description="Scrapes a DJ's playlist from the CHIRP radio \
                                                 (http://chirpradio.org/) and creates a Spotify playlist form it.")  
    parser.add_argument('-U', '--uri', required=True, help='set the dj profile url')
    parser.add_argument('-N', '--name', required=True, help='set the name of the playlist')
    parser.add_argument('-F', '--full', help='download the full dj playlist archive', action='store_false')

    # read arguments from the command line
    args = parser.parse_args()

    uri = args.uri
    playlist_name = args.name

    worker_b(uri, playlist_name, most_recent)
    

if __name__ == '__main__':
    main()
