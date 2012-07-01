# Generate 4 images:
#   * perfect slice
#   * noisy slice
#   * mean squared intensity differences
#   * red-blue channel comparison images
# 
from SimpleITK import *
from sys import argv, stdout
from os.path import join, realpath
from os import system, remove

# process command-line args
image_type = argv[1]
assert(image_type in ["colour", "segmentation"])

PROJECT_ROOT = str(realpath(join(__file__, '..', '..')))
BINARY_PATH = "/Users/Matt/Code/imaging/registration/itk_release/"
DUMMY_PATH  = "/Users/Matt/Code/imaging/registration/results/dummy/"
noisy_path = DUMMY_PATH + "200_alpha0.4/HiResPairs/AdjustedTransforms/CenteredAffineTransform_0/HiRes_" + image_type + "_1_8.mha"
perfect_path = DUMMY_PATH + "perfect_200_alpha0.4/HiResTransforms_4_32/CenteredAffineTransform/HiRes_" + image_type + "_1_8.mha"

# extract slices
# have to use vanilla ITK binary, as SimpleITK doesn't support extraction of vector images
def extract_slice(volume_path, slice_number):
    # paths
    slice_dir = join(PROJECT_ROOT, "Ch7/Figs/dummies")
    slice_path = join(slice_dir, "%03d.tiff" % slice_number)
    
    # use binary to extract slice
    system(BINARY_PATH + "SplitVolumeIntoSlices " +
           volume_path + " " + 
           slice_dir + " " +
           "--sliceDimension 2 " +
           "--outputExtension tiff " +
           "--latex " +
           "--slice " + str(slice_number)
           )
    
    # read and crop slice image and remove file
    slice_image = ReadImage(slice_path)
    remove(slice_path)
    return slice_image

stdout.write("extracting slices...")
slice_number = 99
noisy_slice   = extract_slice(noisy_path,   slice_number)
perfect_slice = extract_slice(perfect_path, slice_number)
stdout.write("done.\n")

# crop images
# have to use vanilla ITK binary, as SimpleITK doesn't support extraction of vector images
def crop_slice(slice_image, index, size):
    WriteImage(slice_image, "./temp.mha")
    system(BINARY_PATH + "CropImage " +
        "./temp.mha ./temp.mha " +
        str(index[0]) + " " +
        str(index[1]) + " " +
        str(size[0]) + " " +
        str(size[1])
    )

    cropped_image = ReadImage("./temp.mha")
    return cropped_image


stdout.write("cropping images...")
noisy_slice   = crop_slice(noisy_slice,   [155, 171], [424, 455])
perfect_slice = crop_slice(perfect_slice, [155, 171], [424, 455])
stdout.write("done.\n")

# mean squared difference slice
stdout.write("calculating squared difference...")
noisy_scalar_slice   = VectorMagnitude(noisy_slice)
perfect_scalar_slice = VectorMagnitude(perfect_slice)
squared_diff = SquaredDifference(noisy_scalar_slice, perfect_scalar_slice)
stdout.write("done.\n")

print "squared difference stats:"
print Statistics(squared_diff)

# define output basepaths
images_path = join(PROJECT_ROOT, 'Ch7/Figs/dummies/')
noisy_basepath        = images_path + image_type + '_noisy_slice'
perfect_basepath      = images_path + image_type + '_perfect_slice'
squared_diff_basepath = images_path + image_type + '_squared_diff'
red_blue_basepath     = images_path + image_type + '_red_blue_diff'

stdout.write("writing slices...")
WriteImage(noisy_slice,   noisy_basepath + '.tiff')
WriteImage(perfect_slice, perfect_basepath + '.tiff')
WriteImage(squared_diff, squared_diff_basepath + '.tiff')
stdout.write("done.\n")

# red-blue channel comparison slice
stdout.write("generating red-blue channel comparison slice...")
system(BINARY_PATH + "BuildRedBlueChannelComparison " +
    noisy_basepath    + ".tiff " +
    perfect_basepath  + ".tiff " +
    red_blue_basepath + ".tiff"
)
stdout.write("done.\n")

# convert tiff file to pdf and remove old tiff file
stdout.write("converting to pdfs...")
def convert_to_pdf(basepath):
    tiff_path = basepath + ".tiff"
    pdf_path  = basepath + ".pdf"
    
    system("tiff2pdf " + tiff_path + " > " + pdf_path)
    remove(tiff_path)

for basepath in [noisy_basepath, perfect_basepath, squared_diff_basepath, red_blue_basepath]:
    convert_to_pdf(basepath)
stdout.write("done.\n")
