import sys
from paraview.simple import *

def extract_contour(segmentation_path, contour_path, apply_magnitude_filter=False):
    # build pipeline
    # segmentation = OpenDataFile(segmentation_path())
    segmentation = MetaFileSeriesReader( guiName="segmentation", FileNames=[segmentation_path] )
    sys.stdout.write('Updating segmentation...')
    segmentation.UpdatePipeline()
    print 'done.'
    if apply_magnitude_filter:
        contour_input = Calculator(segmentation, guiName="intensity", Function='mag(MetaImage)', ReplacementValue=0.0, ResultArrayName='Result', ReplaceInvalidResults=1, AttributeMode='point_data', CoordinateResults=0)
        sys.stdout.write('Updating calculator...')
        contour_input.UpdatePipeline()
        print 'done.'
    else:
        contour_input = segmentation
    
    # intensity is either (3 * 255^2)^0.5, or 1
    if apply_magnitude_filter:
        magnitude = 420.0
    else:
        magnitude = 0.5
    print "magnitude: " magnitude
    
    contour = Contour(contour_input, guiName="contour", Isosurfaces=[magnitude], ComputeNormals=1, ComputeGradients=0, ComputeScalars=0, ContourBy=['POINTS', 'Result'], PointMergeMethod="Uniform Binning")
    contour.PointMergeMethod.Numberofpointsperbucket = 8
    contour.PointMergeMethod.Divisions = [50, 50, 50]
    sys.stdout.write('Updating contour...')
    contour.UpdatePipeline()
    print 'done.'
    
    # write out data file in given format
    writer = XMLPolyDataWriter(contour, FileName=contour_path, CompressorType='ZLib')
    sys.stdout.write('Updating writer...')
    writer.UpdatePipeline()
    print 'done.'
    
    # clean up
    Delete(writer)
    Delete(contour)
    Delete(contour_input)
    del writer, contour, contour_input
    # delete segmentation if not already deleted as contour_input
    if apply_magnitude_filter:
        Delete(segmentation)
        del segmentation
