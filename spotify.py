#! /usr/bin/env python3
# encoding: utf-8

import sys
import config
import spotipy
import spotipy.util as util

class Spotify(object):
    '''
    Spotify class connects up to the Spotify API via Spotipy
    '''
    def __init__(self):
        self.username = config.SPOTIFY_USERNAME
        self.app_client_secret = config.SPOTIFY_CLIENT_SECRET
        self.app_client_id = config.SPOTIFY_CLIENT_ID
        self.scope = config.SPOTIFY_SCOPE
        self.redirect_uri = config.SPOTIFY_REDIRECT_URI
        self.token = util.prompt_for_user_token(self.username,self.scope,client_id=self.app_client_id,client_secret=self.app_client_secret,redirect_uri=self.redirect_uri)

    def add_track(self, artist, track, playlist_id):
        '''
        Adds a track to the specified Spotify playlist
        '''

        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            sp.trace = False
            
            q = 'artist:'+ artist + ' track:' + track
            result = sp.search(q, limit=1, offset=0, type='track', market=None)
            if(result["tracks"]["total"] > 0):
                uri = result["tracks"]["items"][0]["uri"]
                tracks = [
                    uri
                ]
                add_results = sp.user_playlist_add_tracks(self.username, playlist_id, tracks)
                return add_results

        return None

    def create_playlist(self, playlist_name):
        print("Creating new playlist...")
        sp = spotipy.Spotify(auth=self.token)
        sp.trace = False
        playlist_id = 0
        my_playlists = sp.current_user_playlists()
        for i, playlist in enumerate(my_playlists['items']):
            if(playlist_name.lower() == playlist["name"]):
                playlist_id = playlist["id"]
                print("Using existing playlist", playlist_name)
                break
        if playlist_id == 0:
            playlist_id = sp.user_playlist_create(self.username, playlist_name)
            print("Created new playlist", playlist_name)
        return playlist_id

    def read_playlist(self, playlist_id):
        sp = spotipy.Spotify(auth=self.token)
        sp.trace = False
        return sp.user_playlist(self.username, playlist_id)
        