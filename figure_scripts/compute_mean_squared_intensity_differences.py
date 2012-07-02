from os.path import join, realpath
from mpl_toolkits.mplot3d import Axes3D
from sys import argv
from os import path
from SimpleITK import *
import matplotlib.pyplot as plt
import numpy as np

# constants
PROJECT_ROOT = str(realpath(join(__file__, '..', '..')))
FIGURE_PATH = str(join(PROJECT_ROOT, 'Ch7/Figs/dummies/'))
DUMMY_PATH = '/Users/Matt/Code/imaging/registration/results/dummy'

# plain, rotation, translation, rotation + translation
regimes = ('', 'r', 't', 'rt')

# process command-line args
image_type = argv[1]
assert(image_type in ["colour", "segmentation"])

def noisy_volume_path(regime, iteration):
    unicode_str = path.join(DUMMY_PATH,
      '200_alpha0.4' + regime,
      'HiResPairs/AdjustedTransforms/CenteredAffineTransform_' + str(iteration),
      'HiRes_' + image_type + '_4_32.mha')
    # ReadImage only accepts ASCII strings
    return str(unicode_str)

def perfect_volume_path(regime):
    unicode_str = path.join(DUMMY_PATH,
      'perfect_200_alpha0.4' + regime,
      'HiResTransforms_4_32/CenteredAffineTransform/HiRes_' + image_type + '_4_32.mha')
    # ReadImage only accepts ASCII strings
    return str(unicode_str)

# calculate the mean pixel intensity in a slice of a volume
def slice_mean(volume, slice_number):
    # construct size and index of slice
    size = list(volume.GetSize())
    size[2] = 0
    index = [0,0,slice_number]
    
    slice = Extract(volume, size, index)
    stats = Statistics(slice)
    return stats.asdict()['Mean']

# calculate the mean pixel intensities of all slices in the volume
def slice_means(regime, iteration):
    # read diffused and ground truth volumes
    noisy_rgb_volume   = ReadImage(noisy_volume_path(regime, iteration))
    perfect_rgb_volume = ReadImage(perfect_volume_path(regime))
    
    # calculate their scalar intensities
    noisy_volume   = VectorMagnitude(noisy_rgb_volume)
    perfect_volume = VectorMagnitude(perfect_rgb_volume)
    
    # calculate their pixelwise intensity difference
    diff = SquaredDifference(noisy_volume, perfect_volume)
    
    return [slice_mean(diff, slice_number) for slice_number in range(diff.GetDepth())]
    
# compute the mean pixel value of each slice for each iteration
# structure is all_slice_means[regime][iteration][slice]
for regime in regimes:
    regime_slice_means = [slice_means(regime, iteration) for iteration in range(11)]
    regime_slice_means = np.array(regime_slice_means)
    
    # plot comparison of 0th and last iteration
    fig2D = plt.figure(frameon=False)
    ax2D = fig2D.add_subplot(111)
    plt.hold(True)
    labels={0: 'before smoothing', 10: '10th smoothing iteration'}
    
    for i in [0, 10]:
        ax2D.plot(regime_slice_means[i], label=labels[i])
    
    plt.xlabel('Slice Number', fontsize='large')
    plt.ylabel('Pixel Mean Squared Difference', fontsize='large')
    
    fig2D.savefig(join(FIGURE_PATH, image_type + '_mean_square_differences_2D' + regime + '.pdf'))
    
    # plot 3D lines of mean squared differences for each slice
    fig3D = plt.figure(frameon=False)
    ax3D = fig3D.add_axes([0.02,0.02,0.96,0.96], projection='3d')
    # ax3D = fig3D.gca(projection='3d')
    
    # for each image slice
    for slice_number in range(regime_slice_means.shape[1]):
        slice_diffs = regime_slice_means[:,slice_number]
        x = range(len(slice_diffs))
        y = [slice_number + 1] * len(slice_diffs)
        ax3D.plot(x, y, slice_diffs, label="slice %d"%slice_number)
        
    plt.xlabel("Iteration", fontsize='large')
    plt.ylabel("Slice Number", fontsize='large')
    ax3D.set_zlabel("Pixel Mean Sq. Diff.", fontsize='large')
    # ax3D.legend()
    fig3D.savefig(join(FIGURE_PATH, image_type + '_mean_square_differences_3D' + regime + '.pdf'))
