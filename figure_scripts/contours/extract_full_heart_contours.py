#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

import paths, contours

for directory in paths.segmentation_dirs.values():
    print directory
    segmentation_path = directory + "HiRes_1_64_segmentation_240_removed_label_objects.mha"
    contour_path      = directory + "HiRes_1_64_segmentation_240_removed_label_objects_contour.vtp"
    contours.extract_contour(segmentation_path, contour_path, rgb_data=False)
