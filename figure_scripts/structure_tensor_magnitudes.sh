#!/bin/zsh
RESULTS_ROOT=/Users/matt/Code/imaging/registration/results/Rat28/bottom_vessels/HiResPairs/AdjustedTransforms/CenteredAffineTransform_20
DOWNSAMPLES_DIR=downsamples_1_16
RESULTS_PATH=$RESULTS_ROOT/$DOWNSAMPLES_DIR
FIGURES_PATH=/Users/matt/Documents/DPhil/written_work/thesis/Ch7/Figs

set -e

cd $RESULTS_PATH

ApplyStructureTensor HiRes.mha HiRes_ST.vtk 3 50
ExtractLargestEigenvectorComponentsFromTensor ./HiRes_ST.vtk
for i in 0 1 2
do
  SplitVolumeIntoSlices eigencomponent$i.mha eigencomponent$i --pixelType covariantVector --sliceDimension 2 --outputExtension mha
  IntensifyImage --no-invert eigencomponent${i}/0045{.mha,_maxed.png}
done

# volumewise pixel maxima -> scaled up to 255
# 0: 15.39   -> 55.5797890646133
# 1: 39.91   -> 144.13186364968917
# 2: 70.6093 -> 255.0
IntensifyImage eigencomponent0/0045.{mha,png} --no-invert --max=56
IntensifyImage eigencomponent1/0045.{mha,png} --no-invert --max=144
IntensifyImage eigencomponent2/0045.{mha,png} --no-invert --max=255

BuildRGBImage ./eigencomponent{0..2}/0045.png rgb_eigencomponents.png

# copy results to thesis
mv $RESULTS_PATH/eigencomponent0/0045.png $FIGURES_PATH/x_eigencomponent.png
mv $RESULTS_PATH/eigencomponent1/0045.png $FIGURES_PATH/y_eigencomponent.png
mv $RESULTS_PATH/eigencomponent2/0045.png $FIGURES_PATH/z_eigencomponent.png
mv $RESULTS_PATH/rgb_eigencomponents.png $FIGURES_PATH
