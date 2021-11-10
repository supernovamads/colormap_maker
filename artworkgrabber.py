#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:23:27 2021

@author: madvsmit
"""
import requests
import json
import urllib.request
from urllib.parse import quote
import logging
import http.client


def artist_album_grabber(artist,album):
    query_term = "%s %s" % (artist, album)
    url = "https://itunes.apple.com/search?term=%s&media=music&entity=album" % quote(query_term)
    
    
    
    # http.client.HTTPConnection.debuglevel = 1
    
    # # You must initialize logging, otherwise you'll not see debug output.
    # logging.basicConfig()
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests.packages.urllib3")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True
    
    
    
    
    response = requests.get(url,timeout=5).json()
    
    
    artwork_url = response['results'][0]['artworkUrl60']
    print('FOUND THE ARTWORK AT : '+str(artwork_url))
    print('NOW DOWNLOADING THE ARTWORK')
    
    artwork_request = urllib.request.urlopen(artwork_url, timeout=5).read()
    artwork_filename = 'artwork/'+artist.replace(' ','').lower()+'_'+''.join(jk for jk in album if jk.isalnum())+'.jpg'
    with open(artwork_filename, 'wb') as f:
        try:
            f.write(artwork_request)
            print('ARTWORK WAS DOWNLOADED TO ARTWORK DIRECTORY')
        except:
            print('error')
            
    return artwork_filename