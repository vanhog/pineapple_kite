#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:27:52 2024

@author: hog
"""

from kite import Scene
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import cm, colors

#scene = Scene.load('/media/hog/docCrucial1T/tools/nextcloud/kandidat/Roenne_grond/first_attempt/sandbox/tl5_l2a_d_066_02_mscaoi.yml')

#scene = Scene.load('/media/hog/docCrucial1T/tools/nextcloud/kandidat/Roenne_grond/first_attempt/tl5_l2b_a_117_03_mscaoi')
scene = Scene.load('/media/hog/docCrucial1T/tools/nextcloud/kandidat/Roenne_grond/first_attempt/tl5_l2b_d_066_02_mscaoi_v2.npz')

# For convenience we set an abbreviation to the quadtree
qt = scene.quadtree

# Parametrisation of the quadtree
qt.epsilon = 0.0003 #0.00021        # Variance threshold
qt.nan_allowed = 0.99      # Percentage of NaN values allowed per tile/leave

# Be careful here, if you scene is referenced in degree use decimal values!
qt.tile_size_max = 5800  # Maximum leave edge length in [m] or [deg]
qt.tile_size_min = 50 #50    # Minimum leave edge length in [m] or [deg]

print(qt.reduction_rms)   # In units of [m] or [deg]
# >>> 0.234123152

fig = plt.figure()
ax = fig.gca()

limit = np.abs(qt.leaf_medians).max()
print(len(qt.leaf_medians))
color_map = cm.ScalarMappable(
    norm=colors.Normalize(vmin=-limit, vmax=limit),
    cmap=cm.get_cmap('RdBu'))

for rect, leaf in zip(qt.getMPLRectangles(), qt.leaves):
    color = color_map.to_rgba(leaf.median)
    rect.set_facecolor(color)
    rect.set_edgecolor('black')
    ax.add_artist(rect)

ax.set_xlim(qt.leaf_eastings.min(), qt.leaf_eastings.max())
ax.set_ylim(qt.leaf_northings.min(), qt.leaf_northings.max())

plt.show()

#fig2 = plt.figure()
#bx = fig2.gca()

# Inspect the noise data which is used to calculate the covariance
#ax.imshow(scene.covariance.noise_data)
#plt.show()

# Inspect the focal-point (quick mode) covariance matrix
#covfoc = scene.covariance.covariance_matrix_focal
#bx.imshow(covfoc)
#plt.show()

fig3 = plt.figure()
cx = fig3.gca()
covfull = scene.covariance.covariance_matrix
cx.imshow(covfull)
plt.show()
#scene.save('/media/hog/docCrucial1T/tools/nextcloud/kandidat/Roenne_grond/first_attempt/tl5_l2b_a_117_02_mscaoi_covfoc_v2')
#Inspect the full covariance matrix
#bx.imshow(scene.covariance.covariance_matrix)
#plt.show()
# Get the full weight matrix
#ax.imshow(scene.covariance.weight_matrix)

# Get the covariance and weight between two leafes
#leaf_1 = scene.quadtree.leaves[0]
#leaf_2 = scene.quadtree.leaves[0]

#scene.covariance.getLeafCovariance(leaf_1, leaf_2)
#scene.covariance.getLeafWeight(leaf_1, leaf_2)