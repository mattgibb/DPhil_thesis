import sys
import vtk

def extract_contour(segmentation_path, contour_path, rgb_data=False):
    # build pipeline
    sys.stdout.write('Updating segmentation...'); sys.stdout.flush()
    segmentation = vtk.vtkMetaImageReader()
    segmentation.SetFileName(segmentation_path)
    segmentation.Update()
    print 'done.'
    
    if rgb_data:
        calculator_function = "mag(MetaImage)"
    else:
        calculator_function = "MetaImage * 255"
    
    sys.stdout.write('Updating calculator...'); sys.stdout.flush()
    calculator = vtk.vtkArrayCalculator()
    calculator.SetInputConnection(segmentation.GetOutputPort())
    # Working on point data
    calculator.SetAttributeModeToUsePointData()
    calculator.AddScalarArrayName("MetaImage")
    # magnitude of input
    calculator.SetFunction("mag(MetaImage)")
    # The output array will be called resArray
    calculator.SetResultArrayName("magnitude")
    
    # Use AssignAttribute to make resArray the active scalar field
    aa = vtk.vtkAssignAttribute()
    aa.SetInputConnection(calculator.GetOutputPort())
    aa.Assign("magnitude", "SCALARS", "POINT_DATA")
    aa.Update()
    print 'done.'
    
    # intensity is either (3 * 255^2)^0.5, or 1
    if rgb_data:
        magnitude = 420.0
    else:
        magnitude = 127
    
    sys.stdout.write('Updating contour...'); sys.stdout.flush()
    contour = vtk.vtkContourFilter()
    contour.SetInputConnection(calculator.GetOutputPort())
    contour.SetValue(0, magnitude)
    contour.Update()
    print 'done.'
    
    # write out data file in given format
    sys.stdout.write('Updating writer...'); sys.stdout.flush()
    writer = vtk.vtkXMLPolyDataWriter()
    writer.SetFileName(contour_path)
    writer.SetCompressorTypeToZLib()
    writer.SetInputConnection(contour.GetOutputPort())
    writer.Write()
    print 'done.'
