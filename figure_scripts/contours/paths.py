# path helpers
results_root = "/Users/matt/Code/imaging/registration/results/"
dummy_root   = results_root + "dummy/"
Rat28_root   = results_root + "Rat28/"
thesis_root  = "/Users/Matt/Documents/DPhil/written_work/thesis/"

segmentation_dirs = {
    'geometric': Rat28_root + "geometric/HiResTransforms_1_8/CenteredRigid2DTransform/",
    'rigid':     Rat28_root + "rigid/HiResTransforms_1_8/CenteredRigid2DTransform/",
    'size':      Rat28_root + "size/HiResTransforms_1_8/CenteredSimilarity2DTransform/",
    'affine':    Rat28_root + "affine/HiResTransforms_1_8/CenteredAffineTransform/",
    'diffused':  Rat28_root + "affine/HiResPairs/AdjustedTransforms/CenteredAffineTransform_20/"
}

def noisy_path(experiment, iteration):
    return dummy_root + experiment + "/HiResPairs/AdjustedTransforms/CenteredAffineTransform_" + str(iteration) + "/"

def perfect_path(experiment):
    return dummy_root + "perfect_" + experiment + "/HiResTransforms_1_8/CenteredAffineTransform/"
    