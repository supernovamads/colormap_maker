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
from scipy.cluster.vq import whiten

album_loc = 'artwork/dreamland.png'
album = img.imread(album_loc)

album_reshape = np.reshape(album,(np.shape(album)[0]*np.shape(album)[1],4))
color_df = pd.DataFrame({'r':album_reshape.T[0],
                        'g':album_reshape.T[1],
                        'b':album_reshape.T[2]})

color_df['r_scaled'] = whiten(color_df['r'])
color_df['g_scaled'] = whiten(color_df['g'])
color_df['b_Scaled'] = whiten(color_df['b'])

