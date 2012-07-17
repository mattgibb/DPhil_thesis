#!/bin/bash
# script to generate banana cross-sections

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_banana_slice()
{
  # build arguments
  DIM=$1
  SLICE=$2
  VOLUME_PATH=results/Rat28/banana/HiResPairs/BananaTransforms/CenteredRigid2DTransform_banana/HiRes_1_8_cropped.mha
  TIFF_PATH=Ch7/Figs/$SLICE.tiff
  PDF_PATH=Ch7/Figs/banana_${DIM}_${SLICE}.pdf
  
  # generate slice
  extract_slice $VOLUME_PATH Ch7/Figs $DIM $SLICE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

# perform cropping
generate_banana_slice $iteration 0 343
generate_banana_slice $iteration 1 301
