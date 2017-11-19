#! /usr/bin/env python3
# encoding: utf-8

import sys
import datetime
from spotify import Spotify
from chirpScraper import Scrape
import json
def main(uri, playlist_name):
    
    spotify = Spotify()
    playlist_id = spotify.create_playlist(playlist_name)
    
    #TODO: remove or don't allow duplicates
    #existing_playlist = spotify.read_playlist(playlist_id)

    scrape = Scrape(uri)
    tracks = scrape.get_tracks()

    for track in tracks:
        artist = track["artist"]
        track = track["song"]
        result = spotify.add_track(artist, track, playlist_id)

        if result is None:
            print ("Unable to add track", track, "by", artist)
        else:
            print ("Successfully added track")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        uri = sys.argv[1]
        playlist_name = "Chirpify " + str(datetime.datetime.now())
        if(sys.argv[2] is not None):
            playlist_name = sys.argv[2]
    else:
        print ("Whoops, need a playlist uri!")
        print ("usage: python main.py [playlistUri] [playlist name (optional)]")
        sys.exit()

    main(uri, playlist_name)