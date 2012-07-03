#!/bin/bash
# script to generate transverse slices of dummy diffusion experiments

# source constants.sh relative to this file
. $( cd "$( dirname "$0" )" && pwd )/init.sh

copy() {
  INPUT_IMAGE=$REGISTRATION_PATH/images/Rat28/$1/downsamples_$2/0582.bmp
  OUTPUT_IMAGE=$THESIS_PATH/Ch6/Figs/$1_downsamples_$2_0582_zoom.png
  $BINARY_PATH/ConvertImage $INPUT_IMAGE $OUTPUT_IMAGE rgb 2
}

rotate_and_flip() {
  IMAGE=$THESIS_PATH/Ch6/Figs/$1_downsamples_$2_0582_zoom.png
  $BINARY_PATH/RotateImage $IMAGE $IMAGE
  $BINARY_PATH/FlipImage   $IMAGE $IMAGE
}

crop() {
  case $1 in
   LoRes_rgb) REGION=(900 1100 60 60) ;;
   HiRes) REGION=(7000 590 1000 1140) ;;
   *) echo crop was called with the wrong arguments; exit 1 ;;
  esac
  IMAGE=$THESIS_PATH/Ch6/Figs/$1_downsamples_$2_0582_zoom.png
  $BINARY_PATH/CropImage $IMAGE $IMAGE \
    $(expr ${REGION[0]} / $2) \
    $(expr ${REGION[1]} / $2) \
    $(expr ${REGION[2]} / $2) \
    $(expr ${REGION[3]} / $2)
}

copy_rotate_flip_and_crop() {
  copy            $1 $2
  rotate_and_flip $1 $2
  crop            $1 $2
}

copy_and_crop() {
  copy $1 $2
  crop $1 $2
}

# Original HiRes

copy_rotate_flip_and_crop HiRes 1
copy_rotate_flip_and_crop HiRes 8
copy_rotate_flip_and_crop HiRes 64
copy_and_crop LoRes_rgb 1
copy_and_crop LoRes_rgb 8
