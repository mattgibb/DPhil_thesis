import sys
from paraview.simple import *

def extract_contour(segmentation_path, contour_path, rgb_data=False):
    # build pipeline
    # segmentation = OpenDataFile(segmentation_path())
    segmentation = MetaFileSeriesReader( guiName="segmentation", FileNames=[segmentation_path] )
    sys.stdout.write('Updating segmentation...'); sys.stdout.flush()
    segmentation.UpdatePipeline()
    print 'done.'
    if rgb_data:
        calculator_function = "mag(MetaImage)"
    else:
        calculator_function = "MetaImage * 255"
    
    calculator = Calculator(segmentation, guiName="intensity", Function=calculator_function, ReplacementValue=0.0, ResultArrayName='contour_input', ReplaceInvalidResults=1, AttributeMode='point_data', CoordinateResults=0)
    sys.stdout.write('Updating calculator...'); sys.stdout.flush()
    calculator.UpdatePipeline()
    print 'done.'
    
    # intensity is either (3 * 255^2)^0.5, or 1
    if rgb_data:
        magnitude = 220.0
    else:
        magnitude = 127
    
    sys.stdout.write('Updating contour...'); sys.stdout.flush()
    contour = Contour(calculator, guiName="contour", Isosurfaces=[magnitude], ComputeNormals=1, ComputeGradients=0, ComputeScalars=0, ContourBy=['POINTS', 'contour_input'], PointMergeMethod="Uniform Binning")
    contour.PointMergeMethod.Numberofpointsperbucket = 8
    contour.PointMergeMethod.Divisions = [50, 50, 50]
    
    contour.UpdatePipeline()
    print 'done.'
    
    # write out data file in given format
    writer = XMLPolyDataWriter(contour, FileName=contour_path, CompressorType='ZLib')
    sys.stdout.write('Updating writer...'); sys.stdout.flush()
    writer.UpdatePipeline()
    print 'done.'
    
    # # clean up
    Delete(writer)
    Delete(contour)
    Delete(calculator)
    Delete(segmentation)
    del writer, contour, calculator, segmentation
 