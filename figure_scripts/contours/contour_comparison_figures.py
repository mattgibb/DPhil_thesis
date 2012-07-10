#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

from paraview.simple import *

from paths import *
from state import *

paraview.simple._DisableFirstRenderCameraReset()

create_render_view()

for extension in ("", "r", "t", "rt"):
    for iteration in (0,10):
        # load contours
        extension = "rt"
        experiment = "200_alpha0.4" + extension
        noisy_contour   = XMLPolyDataReader( guiName="noisy_contour",   PointArrayStatus=['MetaImage', 'Normals'], CellArrayStatus=[], FileName=[noisy_path(experiment, iteration) + 'HiRes_segmentation_1_8_contour.vtp'] )
        perfect_contour = XMLPolyDataReader( guiName="perfect_contour", PointArrayStatus=['MetaImage', 'Normals'], CellArrayStatus=[], FileName=[perfect_path(experiment)  + 'HiRes_segmentation_1_8_contour.vtp'] )
        
        # set display properties
        noisy_dp   = set_display_properties(noisy_contour)
        perfect_dp = set_display_properties(perfect_contour)
        noisy_dp.ScaleFactor = perfect_dp.ScaleFactor = 3980.0
        noisy_dp.DiffuseColor   = [1.0, 0.3568627450980392, 0.0]
        perfect_dp.DiffuseColor = [0.0, 1.0, 0.19215686274509805]
        
        Show(noisy_contour)
        Show(perfect_contour)
        
        Render()
        
        # save figures
        WriteImage( thesis_root + "Ch7/Figs/dummies/contours/whole_surface%s_%d.png" % (extension,iteration) )
        
        # clean up
        Delete(noisy_contour)
        Delete(perfect_contour)
