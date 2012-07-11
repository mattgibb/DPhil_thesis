#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

import paths, contours

directory = paths.Rat28_root + "affine/ColourResamples_1_8/"
segmentation_path = directory + "LoRes_segmentation_removed_label_objects.mha"
contour_path      = directory + "LoRes_segmentation_removed_label_objects_contour.vtp"
contours.extract_contour(segmentation_path, contour_path, rgb_data=False)
