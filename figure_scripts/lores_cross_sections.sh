#!/bin/bash
# script to generate lores transverse slices
# with and without adjustments

THESIS_PATH=$( cd "$( dirname "$0" )/.." && pwd )
REGISTRATION_PATH="/Users/Matt/Code/imaging/registration/"
BINARY_PATH="$REGISTRATION_PATH/itk_release/"

# compile binaries
( cd $BINARY_PATH && make  )


generate_slice()
{
  VOLUME=$1
  DIM=$2
  SLICE=$3
  $BINARY_PATH/SplitVolumeIntoSlices \
    $REGISTRATION_PATH/results/Rat28/affine/ColourResamples_1_8/$VOLUME.mha \
    $THESIS_PATH/Ch6/Figs -e tiff -l -s $SLICE -d $DIM
  
  TIFF_PATH=$THESIS_PATH/Ch6/Figs/$SLICE.tiff
  # vertical flip, composed of a horizontal flip and 2 90 degree rotations
  $BINARY_PATH/RotateImage $TIFF_PATH $TIFF_PATH
  $BINARY_PATH/RotateImage $TIFF_PATH $TIFF_PATH
  $BINARY_PATH/FlipImage   $TIFF_PATH $TIFF_PATH
  tiff2pdf $TIFF_PATH > $THESIS_PATH/Ch6/Figs/${VOLUME}_${DIM}_${SLICE}.pdf
  rm $THESIS_PATH/Ch6/Figs/$SLICE.tiff
}

generate_slice LoRes_without_adjustments 0 235
generate_slice LoRes_without_adjustments 1 287
generate_slice LoRes                     0 235
generate_slice LoRes                     1 287
