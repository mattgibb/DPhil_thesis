#!/bin/bash
# script to generate transverse slices of dummy diffusion experiments

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_slice()
{
  # build arguments
  EXPERIMENT=$1
  ITERATION=$2
  DIM=$3
  SLICE=$4
  VOLUME_PATH=results/dummy/$EXPERIMENT/HiResPairs/AdjustedTransforms/CenteredAffineTransform_$ITERATION/HiRes.mha
  TIFF_PATH=Ch7/Figs/$SLICE.tiff
  PDF_PATH=Ch7/Figs/dummies/cross_section_${EXPERIMENT}_${ITERATION}_${DIM}_${SLICE}.pdf
  
  # generate slices
  extract_slice $VOLUME_PATH Ch7/Figs $DIM $SLICE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

# generate 2 perpendicular cross-sections for each experiment and iteration
for experiment in 200_alpha0.4{,r,t,rt}; do
  for iteration in {0,1,3,10}; do
    echo experiment: $experiment, iteration: $iteration
    generate_slice $experiment $iteration 0 088
    generate_slice $experiment $iteration 1 107
    echo
  done
done
