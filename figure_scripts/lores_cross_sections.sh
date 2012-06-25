#!/bin/bash
# script to generate lores transverse slices
# with and without adjustments

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

generate_slice()
{
  # build arguments
  VOLUME=$1
  DIM=$2
  SLICE=$3
  TIFF_PATH=Ch6/Figs/$SLICE.tiff
  PDF_PATH=Ch6/Figs/${VOLUME}_${DIM}_${SLICE}.pdf
  
  # generate slice
  extract_slice results/Rat28/affine/ColourResamples_1_8/$VOLUME.mha Ch6/Figs $DIM $SLICE
  flip_and_convert_slice $TIFF_PATH $PDF_PATH
}

generate_slice LoRes_without_adjustments 0 235
generate_slice LoRes_without_adjustments 1 287
generate_slice LoRes                     0 235
generate_slice LoRes                     1 287
