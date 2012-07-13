#!/bin/bash
# script to crop diffusion cross-sections

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_zoomed_slice()
{
  # build arguments
  ITERATION=$1
  DIM=$2
  SLICE=$3
  X_INDEX=$4
  X_SIZE=$5
  Y_INDEX=$6
  Y_SIZE=$7
  VOLUME_PATH=results/Rat28/affine/HiResPairs/AdjustedTransforms/CenteredAffineTransform_$ITERATION/HiRes.mha
  TIFF_PATH=Ch7/Figs/$SLICE.tiff
  PDF_PATH=Ch7/Figs/adjusted_${ITERATION}_${DIM}_${SLICE}_zoomed.pdf
  
  # generate slice
  extract_slice $VOLUME_PATH Ch7/Figs $DIM $SLICE
  $BINARY_PATH/CropImage $THESIS_PATH/$TIFF_PATH{,} 2 $X_INDEX $X_SIZE $Y_INDEX $Y_SIZE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

# perform cropping
for iteration in 0 1 20; do
  generate_zoomed_slice $iteration 0 235 75 320 0 101
  generate_zoomed_slice $iteration 1 287 100 268 0 101
done
