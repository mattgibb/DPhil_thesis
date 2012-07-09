#!/Users/Matt/Code/imaging/ParaView_build/bin/pvpython

from paraview.simple import *

from paths import *

paraview.simple._DisableFirstRenderCameraReset()

def create_render_view():
    RenderView = CreateRenderView()
    RenderView.LightSpecularColor = [1.0, 1.0, 1.0]
    RenderView.KeyLightAzimuth = 10.0
    RenderView.UseTexturedBackground = 0
    RenderView.UseLight = 1
    RenderView.CameraPosition = [96409.9849500128, 39278.79941679306, 19900.0]
    RenderView.FillLightKFRatio = 3.0
    RenderView.Background2 = [0.0, 0.0, 0.165]
    RenderView.FillLightAzimuth = -10.0
    RenderView.LODResolution = 50.0
    RenderView.BackgroundTexture = []
    RenderView.InteractionMode = '3D'
    RenderView.StencilCapable = 1
    RenderView.LightIntensity = 1.0
    RenderView.CameraFocalPoint = [9256.735595703125, 10913.612731933594, 19900.0]
    RenderView.ImageReductionFactor = 2
    RenderView.CameraViewAngle = 30.0
    RenderView.CameraParallelScale = 23721.542335677714
    RenderView.EyeAngle = 2.0
    RenderView.HeadLightKHRatio = 3.0
    RenderView.StereoRender = 0
    RenderView.KeyLightIntensity = 0.75
    RenderView.BackLightAzimuth = 110.0
    RenderView.OrientationAxesInteractivity = 0
    RenderView.UseInteractiveRenderingForSceenshots = 0
    RenderView.UseOffscreenRendering = 0
    RenderView.Background = [1, 1, 1]
    RenderView.UseOffscreenRenderingForScreenshots = 0
    RenderView.NonInteractiveRenderDelay = 2
    RenderView.CenterOfRotation = [9256.735595703125, 10913.612731933594, 19900.0]
    RenderView.CameraParallelProjection = 0
    RenderView.CompressorConfig = 'vtkSquirtCompressor 0 3'
    RenderView.HeadLightWarmth = 0.5
    RenderView.MaximumNumberOfPeels = 4
    RenderView.LightDiffuseColor = [1.0, 1.0, 1.0]
    RenderView.StereoType = 'Red-Blue'
    RenderView.DepthPeeling = 1
    RenderView.BackLightKBRatio = 3.5
    RenderView.StereoCapableWindow = 1
    RenderView.CameraViewUp = [0.0, 0.0, 1.0]
    RenderView.LightType = 'HeadLight'
    RenderView.LightAmbientColor = [1.0, 1.0, 1.0]
    RenderView.RemoteRenderThreshold = 3.0
    RenderView.CacheKey = 0.0
    RenderView.UseCache = 0
    RenderView.KeyLightElevation = 50.0
    RenderView.CenterAxesVisibility = 1
    RenderView.MaintainLuminance = 0
    RenderView.StillRenderImageReductionFactor = 1
    RenderView.BackLightWarmth = 0.5
    RenderView.FillLightElevation = -75.0
    RenderView.MultiSamples = 0
    RenderView.FillLightWarmth = 0.4
    RenderView.AlphaBitPlanes = 1
    RenderView.LightSwitch = 0
    RenderView.OrientationAxesVisibility = 0
    RenderView.CameraClippingRange = [67980.05032199436, 121673.4423160954]
    RenderView.BackLightElevation = 0.0
    RenderView.ViewTime = 0.0
    RenderView.OrientationAxesOutlineColor = [1.0, 1.0, 1.0]
    RenderView.LODThreshold = 5.0
    RenderView.CollectGeometryThreshold = 100.0
    RenderView.UseGradientBackground = 0
    RenderView.KeyLightWarmth = 0.6
    RenderView.OrientationAxesLabelColor = [1.0, 1.0, 1.0]
    RenderView.ViewSize = [420, 2000] #[width, height]
    return RenderView

def set_display_properties(source):
    DataRepresentation = GetDisplayProperties(source)
    DataRepresentation.CubeAxesZAxisVisibility = 1
    DataRepresentation.SelectionPointLabelColor = [0.5, 0.5, 0.5]
    DataRepresentation.SelectionPointFieldDataArrayName = 'MetaImage'
    DataRepresentation.SuppressLOD = 0
    DataRepresentation.CubeAxesXGridLines = 0
    DataRepresentation.CubeAxesYAxisTickVisibility = 1
    DataRepresentation.CubeAxesColor = [1.0, 1.0, 1.0]
    DataRepresentation.Position = [0.0, 0.0, 0.0]
    DataRepresentation.BackfaceRepresentation = 'Follow Frontface'
    DataRepresentation.SelectionOpacity = 1.0
    DataRepresentation.SelectionPointLabelShadow = 0
    DataRepresentation.CubeAxesYGridLines = 0
    DataRepresentation.CubeAxesZAxisRange = [0.0, 1.0]
    DataRepresentation.OrientationMode = 'Direction'
    DataRepresentation.Source.TipResolution = 6
    DataRepresentation.ScaleMode = 'No Data Scaling Off'
    DataRepresentation.Diffuse = 1.0
    DataRepresentation.SelectionUseOutline = 0
    DataRepresentation.CubeAxesZTitle = 'Z-Axis'
    DataRepresentation.Specular = 0.1
    DataRepresentation.SelectionVisibility = 1
    DataRepresentation.InterpolateScalarsBeforeMapping = 1
    DataRepresentation.CubeAxesZAxisTickVisibility = 1
    DataRepresentation.Origin = [0.0, 0.0, 0.0]
    DataRepresentation.CubeAxesVisibility = 0
    DataRepresentation.Scale = [1.0, 1.0, 1.0]
    DataRepresentation.SelectionCellLabelJustification = 'Left'
    DataRepresentation.SelectionCellLabelOpacity = 1.0
    DataRepresentation.Source = "Arrow"
    DataRepresentation.Source.Invert = 0
    DataRepresentation.Masking = 0
    DataRepresentation.Opacity = 1.0
    DataRepresentation.LineWidth = 1.0
    DataRepresentation.MeshVisibility = 0
    DataRepresentation.Visibility = 1
    DataRepresentation.SelectionCellLabelFontSize = 18
    DataRepresentation.CubeAxesCornerOffset = 0.0
    DataRepresentation.SelectionPointLabelJustification = 'Left'
    DataRepresentation.SelectionPointLabelVisibility = 0
    DataRepresentation.SelectOrientationVectors = ''
    DataRepresentation.CubeAxesTickLocation = 'Inside'
    DataRepresentation.CubeAxesXAxisMinorTickVisibility = 1
    DataRepresentation.CubeAxesYAxisVisibility = 1
    DataRepresentation.SelectionPointLabelFontFamily = 'Arial'
    DataRepresentation.Source.ShaftResolution = 6
    DataRepresentation.CubeAxesFlyMode = 'Closest Triad'
    DataRepresentation.SelectScaleArray = ''
    DataRepresentation.CubeAxesYTitle = 'Y-Axis'
    DataRepresentation.ColorAttributeType = 'POINT_DATA'
    DataRepresentation.SpecularPower = 100.0
    DataRepresentation.Texture = []
    DataRepresentation.SelectionCellLabelShadow = 0
    DataRepresentation.AmbientColor = [1.0, 1.0, 1.0]
    DataRepresentation.MapScalars = 1
    DataRepresentation.PointSize = 2.0
    DataRepresentation.Source.TipLength = 0.35
    DataRepresentation.SelectionCellLabelFormat = ''
    DataRepresentation.Scaling = 0
    DataRepresentation.StaticMode = 0
    DataRepresentation.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    DataRepresentation.Source.TipRadius = 0.1
    DataRepresentation.EdgeColor = [0.0, 0.0, 0.5000076295109483]
    DataRepresentation.CubeAxesXAxisTickVisibility = 1
    DataRepresentation.SelectionCellLabelVisibility = 0
    DataRepresentation.NonlinearSubdivisionLevel = 1
    DataRepresentation.CubeAxesXAxisRange = [0.0, 1.0]
    DataRepresentation.Representation = 'Surface'
    DataRepresentation.CubeAxesYAxisRange = [0.0, 1.0]
    DataRepresentation.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    DataRepresentation.Orientation = [0.0, 0.0, 0.0]
    DataRepresentation.CubeAxesEnableCustomAxisRange = 0
    DataRepresentation.CubeAxesXTitle = 'X-Axis'
    DataRepresentation.CubeAxesInertia = 1
    DataRepresentation.BackfaceOpacity = 1.0
    DataRepresentation.SelectionCellFieldDataArrayName = 'vtkOriginalCellIds'
    DataRepresentation.SelectionColor = [1.0, 0.0, 1.0]
    DataRepresentation.Ambient = 0.0
    DataRepresentation.SelectionPointLabelFontSize = 18
    DataRepresentation.ScaleFactor = 3980.0
    DataRepresentation.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    DataRepresentation.Source.ShaftRadius = 0.03
    DataRepresentation.SelectMaskArray = ''
    DataRepresentation.SelectionLineWidth = 2.0
    DataRepresentation.CubeAxesZAxisMinorTickVisibility = 1
    DataRepresentation.CubeAxesXAxisVisibility = 1
    DataRepresentation.Interpolation = 'Gouraud'
    DataRepresentation.SelectionCellLabelFontFamily = 'Arial'
    DataRepresentation.SelectionCellLabelItalic = 0
    DataRepresentation.CubeAxesYAxisMinorTickVisibility = 1
    DataRepresentation.CubeAxesZGridLines = 0
    DataRepresentation.SelectionPointLabelFormat = ''
    DataRepresentation.SelectionPointLabelOpacity = 1.0
    DataRepresentation.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
    DataRepresentation.Pickable = 1
    DataRepresentation.CustomBoundsActive = [0, 0, 0]
    DataRepresentation.SelectionRepresentation = 'Wireframe'
    DataRepresentation.SelectionPointLabelBold = 0
    DataRepresentation.ColorArrayName = ''
    DataRepresentation.SelectionPointLabelItalic = 0
    DataRepresentation.AllowSpecularHighlightingWithScalarColoring = 0
    DataRepresentation.SpecularColor = [1.0, 1.0, 1.0]
    DataRepresentation.LookupTable = []
    DataRepresentation.SelectionPointSize = 5.0
    DataRepresentation.SelectionCellLabelBold = 0
    DataRepresentation.Orient = 0
    return DataRepresentation

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
