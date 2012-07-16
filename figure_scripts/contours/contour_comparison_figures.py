#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

from paraview.simple import *

from paths import *
from state import *

paraview.simple._DisableFirstRenderCameraReset()

view = create_render_view()
view.ViewSize = [540, 2000] #[width, height]

for extension in ("", "r", "t", "rt"):
    experiment = "200_alpha0.4" + extension
    print "experiment: " + experiment
    for iteration in (0,1,3,8,20):
        print "iteration: " + str(iteration)
        
        # load contours
        noisy_contour   = XMLPolyDataReader( guiName="noisy_contour",   PointArrayStatus=['MetaImage', 'Normals'], CellArrayStatus=[], FileName=[noisy_path(experiment, iteration) + 'HiRes_segmentation_contour.vtp'] )
        perfect_contour = XMLPolyDataReader( guiName="perfect_contour", PointArrayStatus=['MetaImage', 'Normals'], CellArrayStatus=[], FileName=[perfect_path(experiment)  + 'HiRes_segmentation_contour.vtp'] )
        
        # set display properties
        noisy_dp   = set_display_properties(noisy_contour)
        perfect_dp = set_display_properties(perfect_contour)
        noisy_dp.ScaleFactor = perfect_dp.ScaleFactor = 3980.0
        noisy_dp.DiffuseColor   = [1.0, 0.3568627450980392, 0.0]
        perfect_dp.DiffuseColor = [0.0, 1.0, 0.19215686274509805]
        noisy_dp.Opacity   = 1.0
        perfect_dp.Opacity = 1.0
        
        Show(noisy_contour)
        Show(perfect_contour)
        
        Render()
        
        # save figures
        WriteImage( thesis_root + "Ch7/Figs/dummies/contours/whole_surface%s_%d.png" % (extension,iteration) )
        
        # clean up
        Delete(noisy_contour)
        Delete(perfect_contour)
