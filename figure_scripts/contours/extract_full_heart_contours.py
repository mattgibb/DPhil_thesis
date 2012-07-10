#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

import paths, contours

segmentation_dirs = [
    "geometric/HiResTransforms_1_8/CenteredRigid2DTransform/",
    "rigid/HiResTransforms_1_8/CenteredRigid2DTransform/",
    "size/HiResTransforms_1_8/CenteredSimilarity2DTransform/",
    "affine/HiResTransforms_1_8/CenteredAffineTransform/"
]
  
for directory in segmentation_dirs:
    print directory
    segmentation_path = paths.results_root + "Rat28/" + directory + "HiRes_1_64_segmentation_240_removed_label_objects.mha"
    contour_path      = paths.results_root + "Rat28/" + directory + "HiRes_1_64_segmentation_240_removed_label_objects_contour.vtp"
    contours.extract_contour(segmentation_path, contour_path, apply_magnitude_filter=False)
