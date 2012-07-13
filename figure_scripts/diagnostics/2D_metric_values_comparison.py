#!/usr/bin/python
# paths
registration_root = "/Users/Matt/Code/imaging/registration/"
Rat28_root = registration_root + "results/Rat28/"
thesis_root = "/Users/Matt/Documents/DPhil/written_work/thesis/"

import sys
from os import listdir
from numpy import *
import matplotlib.pyplot as plt

# add registration graphing directory to python path
sys.path.insert(0, registration_root + "graphing")

from metric_values import MetricValues

# metric values dirs
metric_value_dir = registration_root + "results/Rat28/%s/MetricValues/"
rigid_values      = MetricValues(metric_value_dir % "rigid" + "CenteredRigid2DTransform" )
similarity_values = MetricValues(metric_value_dir % "size" + "CenteredSimilarity2DTransform")
affine_values     = MetricValues(metric_value_dir % "affine" + "CenteredAffineTransform")

# check that they all have the same number of slices
assert(rigid_values.number_of_slices() == similarity_values.number_of_slices() == affine_values.number_of_slices())
x = range(rigid_values.number_of_slices())

# plot figure
fig = plt.figure(frameon=False)
ax = fig.add_axes([0.05,0.05,0.9,0.9])
ax.plot(x, rigid_values.initial_values(), label="Initial values")
ax.plot(x, rigid_values.final_values(), label="Final rigid values")
ax.plot(x, similarity_values.final_values(), label="Final similarity values")
ax.plot(x, affine_values.final_values(), 'y', label="Final affine values")

plt.xlabel('Curated slice number', fontsize='large')
plt.ylabel('Normalised correlation', fontsize='large')

plt.grid()
ax.legend()
plt.show()
