#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:23:27 2021

@author: madvsmit
"""
import requests
import json
from urllib.parse import quote
import logging
import http.client

artist = 'Portugal the Man'
album= 'Woodstock'

query_term = "%s %s" % (artist, album)
url = "https://itunes.apple.com/search?term=%s&media=music&entity=album" % quote(query_term)



http.client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True




response = requests.get(url,timeout=5).json()


