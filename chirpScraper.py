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
    def __init__(self, dj_uri, most_recent=True):
        self.dj_uri = dj_uri
        self.most_recent = most_recent
    
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
            html = self.get_dj_html(uri)
            soup = BeautifulSoup(html, 'html.parser')
            seed_table = soup.find('table')
            seed_table_rows = seed_table.find_all('tr')
            seed_datetime_raw = seed_table_rows[0].find('td', attrs={'class':'date-heading'})
            seed_datetime = seed_datetime_raw.text.strip()
            seed_date = seed_datetime.split('-')[0].strip()
            while uri:
                html = self.get_dj_html(uri)
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find('table')
                rows = table.find_all('tr')
                date_match = True
                for row in rows:
                    artist = row.find('td', attrs={'class':'artist'})
                    song = row.find('td', attrs={'class':'track'})
                    album = row.find('td', attrs={'class':'album'})
                    if artist and song and album:
                        if '<mark>Local</mark>' in str(artist):
                            artist = artist.text.strip().rstrip('Local')
                        else:
                            artist = artist.text.strip()
                        tracks.append({'artist': artist,
                                       'song': song.text.strip(),
                                       'album': album.text.strip()})
                    if self.most_recent:
                        found_datetime_raw = row.find('td', attrs={'class':'date-heading'})
                        if found_datetime_raw:
                            found_datetime = found_datetime_raw.text.strip()
                            found_date = found_datetime.split('-')[0].strip()
                        if seed_date != found_date:
                            date_match = False
                            break
                if date_match == False:
                    uri = False
                else:
                    pages = soup.find('ol', attrs={'class':'pagination'})
                    try:
                        uri = pages.find('a', attrs={'class':'next'})['href']
                    except:
                        uri = False
                    time.sleep(random.random())
            return tracks
        except self.ScrapeError as e:
            print(e.args)
            return 1
    
    class ScrapeError(Exception):
        '''
        Passes errors
        '''
        pass
    
