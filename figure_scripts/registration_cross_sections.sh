#!/bin/bash
# script to generate lores transverse slices
# with and without adjustments

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_slice()
{
  # build arguments
  TRANSFORM=$1
  TRANSFORM_FULL_NAME=$2
  DIM=$3
  SLICE=$4
  VOLUME_PATH=results/Rat28/$TRANSFORM/HiResTransforms_1_8/$TRANSFORM_FULL_NAME/HiRes.mha
  TIFF_PATH=Ch6/Figs/$SLICE.tiff
  PDF_PATH=Ch6/Figs/${TRANSFORM}_${DIM}_${SLICE}.pdf
  
  # generate slice
  extract_slice $VOLUME_PATH Ch6/Figs $DIM $SLICE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

transforms=(rigid size affine)
transform_full_names=(Centered{{Rigid,Similarity}2D,Affine}Transform)
slices=(235 287)

for i in {0..2}; do
  for dim in 0 1; do
    generate_slice ${transforms[i]} ${transform_full_names[i]} $dim ${slices[$dim]}
  done
done
