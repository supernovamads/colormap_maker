#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 19:02:52 2021

@author: madisonsmith
"""
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.vq import whiten,kmeans
from sklearn.cluster import AffinityPropagation


album_loc = 'artwork/dreamland.png'
album = img.imread(album_loc)

album_reshape = np.reshape(album,(np.shape(album)[0]*np.shape(album)[1],4))
color_df = pd.DataFrame({'r':album_reshape.T[0],
                        'g':album_reshape.T[1],
                        'b':album_reshape.T[2]})

color_df['r_scaled'] = whiten(color_df['r'])
color_df['g_scaled'] = whiten(color_df['g'])
color_df['b_scaled'] = whiten(color_df['b'])

# distortions = []
wanted_colors = 12
# num_clusters = np.arange(1,wanted_colors,1)
# for i in num_clusters:
#     cluster_centers,distortion = kmeans(color_df[['r_scaled','g_scaled','b_scaled']],i)
#     distortions.append(distortion)

X = color_df[['r_scaled','g_scaled','b_scaled']].to_numpy()

cluster_centers, _ = kmeans(color_df[['r','g','b']],wanted_colors)
dominant_colors = []
 
red_std, green_std, blue_std = color_df[['r','g','b']].std()
 
for cluster_center in cluster_centers:
    red_scaled, green_scaled, blue_scaled = cluster_center
    dominant_colors.append(cluster_center)
    # dominant_colors.append((
    #     red_scaled * red_std / 255,
    #     green_scaled * green_std / 255,
    #     blue_scaled * blue_std / 255))


