#!/bin/bash
# script to generate HiRes transverse slices,
# before and after various registrations

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_slice()
{
  # build arguments
  OUTPUT_DIR=$1
  TRANSFORM_FULL_NAME=$2
  DIM=$3
  SLICE=$4
  VOLUME_PATH=results/Rat28/$OUTPUT_DIR/HiResTransforms_1_8/$TRANSFORM_FULL_NAME/HiRes.mha
  TIFF_PATH=Ch6/Figs/$SLICE.tiff
  PDF_PATH=Ch6/Figs/${OUTPUT_DIR}_${DIM}_${SLICE}.pdf
  
  # generate slice
  extract_slice $VOLUME_PATH Ch6/Figs $DIM $SLICE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}


output_dirs=(geometric rigid size affine)
transforms=(Centered{{Rigid{,},Similarity}2D,Affine}Transform)
slices=(235 287)

for i in {0..3}; do
  for dim in 0 1; do
    generate_slice ${output_dirs[i]} ${transforms[i]} $dim ${slices[$dim]}
  done
done
