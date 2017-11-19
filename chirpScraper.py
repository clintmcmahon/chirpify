#! /usr/bin/env python3
# encoding: utf-8

import time
import random
import requests
from bs4 import BeautifulSoup

class Scrape(object):
    '''
    Scrape class scrapes the the CHIRP Radio website
    for a DJs playlist.
    '''
    def __init__(self, dj_uri):
        self.dj_uri = dj_uri
    
    def get_tracks(self):
        '''Returns a list of dictionaries 
        '''
        try:
            return self.make_soup()
        except self.ScrapeError as e:
            print(e.args)
            return 1

    def get_dj_html(self, uri):
        '''
        Gets the HTML for a specified DJ's URI
        '''
        try:
            r = requests.get(uri)
            if r.status_code != 200:
                raise self.ScrapeError('HTTP status code: {}'.format(r.status_code))
            return r.text
        except self.ScrapeError as e:
            print(e.args)
            return 1
    
    def make_soup(self):
        '''
        Takes the HTML output and parses the data with 
        BeautifulSoup
        '''
        try:
            tracks = []
            uri = self.dj_uri
            while uri:
                html = self.get_dj_html(uri)
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find('table')
                rows = table.find_all('tr')
                for row in rows:
                    artist = row.find('td', attrs={'class':'artist'})
                    song = row.find('td', attrs={'class':'track'})
                    album = row.find('td', attrs={'class':'album'})
                    if artist and song and album:
                        tracks.append({'artist': artist.text.strip(),
                                       'song': song.text.strip(),
                                       'album': album.text.strip()})
                pages = soup.find('ol', attrs={'class':'pagination'})
                try:
                    uri = pages.find('a', attrs={'class':'next'})['href']
                except:
                    uri = False
                #time.sleep(random.random())
            return tracks
        except self.ScrapeError as e:
            print(e.args)
            return 1
    
    class ScrapeError(Exception):
        '''
        Passes errors
        '''
        pass
    
