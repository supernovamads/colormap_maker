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

artist = input('Name of artist: ')
album = input('Name of album: ')


album_cover = artist_album_grabber(artist,album)



data = pd.read_csv('test/galaxyproperties.dat',sep='\s+',skiprows=30,names=['name','RA','Dec','distance','T','O/H','O/H_err',
                                                                                'flag_marble','method','A_FUV','flag_hao','logM'])

extracted_colors = colorgram.extract(album_cover,32)[::-1]
extracted_rgb = [(i.rgb.r/255,i.rgb.g/255,i.rgb.b/255) for i in extracted_colors]
album_colormap = mpl.colors.ListedColormap(extracted_rgb)

album_array = mpimg.imread(album_cover)

fig = plt.figure()
ax1 = fig.add_subplot(111)
galaxies = ax1.scatter(data['O/H'],data['logM'],c=data['T'],cmap=album_colormap)

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