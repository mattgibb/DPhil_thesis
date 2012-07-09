# path helpers
dummy_root = "/Users/Matt/Code/imaging/registration/results/dummy/"
thesis_root = "/Users/Matt/Documents/DPhil/written_work/thesis/"

def noisy_path(experiment, iteration):
    return dummy_root + experiment + "/HiResPairs/AdjustedTransforms/CenteredAffineTransform_" + str(iteration) + "/"

def perfect_path(experiment):
    return dummy_root + "perfect_" + experiment + "/HiResTransforms_4_32/CenteredAffineTransform/"
    
