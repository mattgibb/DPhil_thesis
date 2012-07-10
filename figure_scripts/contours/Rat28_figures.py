#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

from paraview.simple import *

from paths import *
from state import *

paraview.simple._DisableFirstRenderCameraReset()

# configure view
view = create_render_view()
view.ViewSize = [3000, 2000] #[width, height]

def save_positive_x_snapshot(name):
    view.CameraPosition = [-17397.295366965835, 7634.2001953125, 4500.0]
    view.CameraFocalPoint = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraParallelScale = 10836.969887782794
    view.CenterOfRotation = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraClippingRange = [10985.622217983677, 39614.95948497032]
    view.CameraViewUp = [0.0, 0.0, 1.0]
    
    # save figures
    WriteImage( thesis_root + "Ch7/Figs/Rat28/contours/whole_positive_x_%s.png" % name )

def save_negative_x_snapshot(name):
    view.CameraPosition = [29872.695757590835, 7634.2001953125, 4500.0]
    view.CameraFocalPoint = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraParallelScale = 10836.969887782794
    view.CenterOfRotation = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraClippingRange = [10985.622217983677, 39614.95948497032]
    view.CameraViewUp = [0.0, 0.0, 1.0]
    
    # save figures
    WriteImage( thesis_root + "Ch7/Figs/Rat28/contours/whole_negative_x_%s.png" % name )

def save_positive_y_snapshot(name):
    view.CameraPosition = [6237.7001953125, -16000.795366965835, 4500.0]
    view.CameraFocalPoint = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraParallelScale = 10836.969887782794
    view.CenterOfRotation = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraClippingRange = [8206.587217983677, 43113.191984970326]
    view.CameraViewUp = [0.0, 0.0, 1.0]
    
    # save figures
    WriteImage( thesis_root + "Ch7/Figs/Rat28/contours/whole_positive_y_%s.png" % name )

def save_positive_z_snapshot(name):
    view.CameraPosition = [6237.7001953125, 7634.200195312501, -24098.344630356787]
    view.CameraFocalPoint = [6237.7001953125, 7634.200195312501, 4500.0]
    view.CameraParallelScale = 10836.969887782794
    view.CenterOfRotation = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraClippingRange = [19357.361184053218, 40299.81979981215]
    view.CameraViewUp = [1.0, 0.0, 0.0]
    
    # save figures
    WriteImage( thesis_root + "Ch7/Figs/Rat28/contours/whole_positive_z_%s.png" % name )

def save_zoom_snapshot(name):
    view.CameraPosition = [-9905.319791217333, 7634.2001953125, 4500.0]
    view.CameraFocalPoint = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraParallelScale = 10836.969887782794
    view.CenterOfRotation = [6237.7001953125, 7634.2001953125, 4500.0]
    view.CameraClippingRange = [3568.5663979926585, 32010.604275585596]
    
    # save figures
    WriteImage( thesis_root + "Ch7/Figs/Rat28/contours/zoom_%s.png" % name )

def save_snapshots(name):
    save_positive_x_snapshot(name)
    save_negative_x_snapshot(name)
    save_positive_y_snapshot(name)
    save_positive_z_snapshot(name)
    
for name, directory in segmentation_dirs.items():
    # load contours
    contour   = XMLPolyDataReader(guiName="noisy_contour",
                                  PointArrayStatus=['MetaImage', 'Normals'],
                                  CellArrayStatus=[],
                                  FileName=[directory + 'HiRes_1_64_segmentation_240_removed_label_objects_contour.vtp'] )
    
    # set display properties
    dp = set_display_properties(contour)
    # dp.ScaleFactor = perfect_dp.ScaleFactor = 3980.0
    
    # display results
    Show(contour)
    Render()
    
    # save snapshots
    save_snapshots(name)
    
    # clean up
    Delete(contour)
