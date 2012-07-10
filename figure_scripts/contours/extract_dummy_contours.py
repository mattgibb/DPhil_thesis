#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

from paths import *
import contours

# create contour in same directory as segmentation
def extract_contour(directory):
    segmentation_path = directory + "HiRes_segmentation_1_8.mha"
    contour_path      = directory + "HiRes_segmentation_1_8_contour.vtp"
    contours.extract_contour(segmentation_path, contour_path, apply_magnitude_filter=True)

# generate all dummy contours
for extension in ("", "r", "t", "rt"):
    experiment = "200_alpha0.4" + extension
    print experiment
    
    # imperfect iterations
    for iteration in range(11):
        print 'iteration: %d'%iteration
        extract_contour(noisy_path(experiment, iteration))
    
    # perfect volumes
    print "perfect volume"
    extract_contour(perfect_path(experiment))
