# define common constants
THESIS_PATH=$( cd "$( dirname "$0" )/.." && pwd )
REGISTRATION_PATH="/Users/Matt/Code/imaging/registration/"
BINARY_PATH="$REGISTRATION_PATH/itk_release/"

# compile binaries
( cd $BINARY_PATH && make )

# extract slice from volume
extract_slice() {
  # build arguments
  VOLUME_FILE=$1
  OUTPUT_DIR=$2
  DIM=$3
  SLICE=$4
  
  $BINARY_PATH/SplitVolumeIntoSlices \
    $REGISTRATION_PATH/$VOLUME_FILE \
    $THESIS_PATH/$OUTPUT_DIR -e tiff -l -d $DIM -s $SLICE
}

# vertical flip raw tiff slices
# usage: flip_and_convert_slice Ch6/Figs/image.tiff

flip_slice() {
  # build arguments
  TIFF_PATH=$THESIS_PATH/$1
  
  # vertical flip, composed of a horizontal flip and 2 90 degree rotations
  $BINARY_PATH/RotateImage $TIFF_PATH $TIFF_PATH
  $BINARY_PATH/RotateImage $TIFF_PATH $TIFF_PATH
  $BINARY_PATH/FlipImage   $TIFF_PATH $TIFF_PATH
}

# convert slice from tiff to pdf
# usage: flip_and_convert_slice Ch6/Figs/image.tiff Ch6/Figs/result.pdf
convert_slice() {
  # build arguments
  TIFF_PATH=$THESIS_PATH/$1
  PDF_PATH=$THESIS_PATH/$2
  
  # convert tiff file to pdf
  tiff2pdf $TIFF_PATH > $PDF_PATH
  rm $TIFF_PATH
}

flip_and_convert_slice() {
  flip_slice $*
  convert_slice $*
}
