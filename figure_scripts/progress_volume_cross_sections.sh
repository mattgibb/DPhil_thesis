#!/bin/bash
# script to generate progress volume transverse slices

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh


generate_slice()
{
  # build arguments
  IMAGE=$1
  FIXED_OR_MOVING=$2
  DIM=$3
  SLICE=$4
  VOLUME_PATH=results/Rat28/rigid/IntermediateTransforms/CenteredRigid2DTransform/$IMAGE/${FIXED_OR_MOVING}_1_8.mha
  TIFF_PATH=Ch6/Figs/$SLICE.tiff
  PDF_PATH=Ch6/Figs/diagnostics/${FIXED_OR_MOVING}_progress_slice_${IMAGE}_${DIM}_${SLICE}.pdf

  # generate slice
  extract_slice $VOLUME_PATH Ch6/Figs $DIM $SLICE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

output_dirs=(geometric rigid size affine)
transforms=(Centered{{Rigid{,},Similarity}2D,Affine}Transform)
slices=(235 287)

for type in fixed moving; do
  generate_slice 0562 $type 0 235
  generate_slice 0562 $type 1 287
done
