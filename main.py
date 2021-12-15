#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:07:02 2021

@author: madisonsmith
"""
import colorgram
#https://github.com/obskyr/colorgram.py
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from artworkgrabber import artist_album_grabber
import requests
import json
import urllib.request
from urllib.parse import quote

#Will eventually want to put all of this in a function because inline inputs are gross
artist = input('Name of artist: ')
album = input('Name of album: ')


album_cover = artist_album_grabber(artist,album)
# album_cover = 'artwork/passionpit.jpg'

class AlbumCover:
    def __init__(self,artist,album,info=None):
        self.artist = artist
        self.album = album
        self.info = info
        self.artworkpath = None
    def info_retriever(self):
        if self.info == None:
            query_term = "%s %s" % (self.artist, self.album)
            url = "https://itunes.apple.com/search?term=%s&media=music&entity=album" % quote(query_term)
            try:
                response = requests.get(url,timeout=5).json()
                self.info = response
            except:
                print('Something went wrong')
        else:
            print('info has already been collected')
            pass
    def download_artwork(self):
        if self.artworkpath == None:
            self.artworkpath = artist_album_grabber(self.artist,self.album)
        else:
            print('Path already exists')
        
data = pd.read_csv('test/galaxyproperties.dat',sep='\s+',skiprows=30,names=['name','RA','Dec','distance','T','O/H','O/H_err',
                                                                                'flag_marble','method','A_FUV','flag_hao','logM'])

extracted_colors = colorgram.extract(album_cover,32)[::-1]
extracted_rgb = [(i.rgb.r/255,i.rgb.g/255,i.rgb.b/255) for i in extracted_colors]
album_colormap = mpl.colors.ListedColormap(extracted_rgb)

album_array = mpimg.imread(album_cover)

fig = plt.figure()
ax1 = fig.add_subplot(111)
galaxies = ax1.scatter(data['O/H'],data['logM'],c=data['T'],cmap=album_colormap)
# ax2 = fig.add_subplot(132)
# galaxies_12 = ax2.scatter(data['O/H'],data['logM'],c=data['T'],cmap=album_colormap)
# ax3 = fig.add_subplot(133)
# galaxies_32 = ax3.scatter(data['O/H'],data['logM'],c=data['T'],cmap=album_colormap_32)

cbar = plt.colorbar(galaxies,ax=ax1)
cbar.ax.set_ylabel('T type')

ax1.set_ylabel('log(M)')
ax1.set_xlabel('12 + log(O/H)')

#putting inset in bottom right corner
bottom_right = [ax1.get_xlim()[1],ax1.get_ylim()[0]]
percent_size = .10
left = bottom_right[0]-percent_size*(ax1.get_xlim()[1]-ax1.get_xlim()[0])
bottom = bottom_right[1]
height = percent_size*(ax1.get_xlim()[1]-ax1.get_xlim()[0])
width = percent_size*(ax1.get_xlim()[1]-ax1.get_xlim()[0])
inset = fig.add_axes([0.525,0.11,0.25,0.25])
inset.imshow(album_array)
plt.setp(inset, xticks=[], yticks=[])


plt.show()