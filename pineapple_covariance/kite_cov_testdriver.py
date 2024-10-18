from kite import Scene
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib import cm, colors

source_scene = Scene.load('/media/hog/docCrucial1T/msc_grond_noemi/volume_opti/data/events/roenne/insar_float32_losturn/tl5_l2b_a_044_01_mscaoi_f32_foccov_losturn.npz')
noisecoords = source_scene.covariance.noise_coord
sourceeps = source_scene.quadtree.epsilon
sourcenan = source_scene.quadtree.nan_allowed
sourcemintile = source_scene.quadtree.tile_size_min
sourcemaxtile = source_scene.quadtree.tile_size_max
#sourceblack   = source_scene.quadtree.config.leaf_blacklist
sourcepolygm  = source_scene.config.polygon_mask
print('noisecoords:\t', noisecoords)
print('eps: \t', sourceeps)
print('nan: \t', sourcenan)
print('tilemin:\t', sourcemintile)
print('tilemax:\t', sourcemaxtile)
print('polyonm:\t', sourcepolygm)
target_scene = Scene.load('/home/hog/data/dev/testdata/kite_qt_scene.npz')
target_scene.config.polygon_mask = sourcepolygm
target_scene.quadtree.epsilon = sourceeps
target_scene.quadtree.nan_allowed = sourcenan
target_scene.quadtree.tile_size_min = sourcemintile
target_scene.quadtree.tile_size_max = sourcemaxtile
#target_scene.quadtree.config.leaf_blacklist = sourceblack
target_scene.covariance.noise_coord = noisecoords
target_scene.save('/home/hog/data/dev/testdata/kite_qt_scene_com.npz')
print('happy days')