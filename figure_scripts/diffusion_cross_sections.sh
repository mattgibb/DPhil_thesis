#!/bin/bash
# script to generate HiRes transverse slices,
# before and after diffusion smoothing

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_slice()
{
  # build arguments
  ITERATION=$1
  DIM=$2
  SLICE=$3
  VOLUME_PATH=results/Rat28/affine/HiResPairs/AdjustedTransforms/CenteredAffineTransform_$ITERATION/HiRes.mha
  TIFF_PATH=Ch7/Figs/$SLICE.tiff
  PDF_PATH=Ch7/Figs/adjusted_${ITERATION}_${DIM}_${SLICE}.pdf
  # generate slice
  extract_slice $VOLUME_PATH Ch7/Figs $DIM $SLICE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

for iteration in 0 1 20; do
  generate_slice $iteration 0 235
  generate_slice $iteration 1 287
done
