#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

from paraview.simple import *

def adjusted_transforms_path(experiment, iteration):
    return "/Users/Matt/Code/imaging/registration/results/dummy/" + experiment + "/HiResPairs/AdjustedTransforms/CenteredAffineTransform_" + str(iteration) + "/"

for extension in ("", "r", "t", "rt"):
    experiment = "200_alpha0.4" + extension
    print experiment
    
    for iteration in range(11):
        print 'iteration: %d'%iteration
        
        # construct paths
        directory = adjusted_transforms_path(experiment, iteration)
        segmentation_path = directory + "HiRes_segmentation_1_8.mha"
        contour_path      = directory + "HiRes_segmentation_1_8_contour.vtp"

        # build pipeline
        # segmentation = OpenDataFile(segmentation_path())
        segmentation = MetaFileSeriesReader( guiName="segmentation", FileNames=[segmentation_path] )
        calc = Calculator( guiName="intensity", Function='mag(MetaImage)', ReplacementValue=0.0, ResultArrayName='Result', ReplaceInvalidResults=1, AttributeMode='point_data', CoordinateResults=0 )
        contour = Contour( guiName="contour", Isosurfaces=[420.0], ComputeNormals=1, ComputeGradients=0, ComputeScalars=0, ContourBy=['POINTS', 'Result'], PointMergeMethod="Uniform Binning" )
        contour.PointMergeMethod.Numberofpointsperbucket = 8
        contour.PointMergeMethod.Divisions = [50, 50, 50]

        # write out data file in given format
        writer = XMLPolyDataWriter(contour, FileName=contour_path, CompressorType='ZLib')
        writer.UpdatePipeline()
        
        # clean up
        Delete(writer)
        Delete(contour)
        Delete(calc)
        Delete(segmentation)
        del writer, contour, calc, segmentation
