import pydensecrf.densecrf as dcrf
import numpy as np
import sys
import os

from skimage.io import imread, imsave
from pydensecrf.utils import unary_from_labels, create_pairwise_bilateral, create_pairwise_gaussian, unary_from_softmax

from os import listdir, makedirs
from os.path import isfile, join

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

davis_path = 'your_path/davis16-test/' #original images
setting = 'your_path/davis/' #your test results
out_folder = 'your_path/davis_crf/' #save your crf results
for d in listdir(setting):
    vidDir = join(davis_path, d)
    resDir = join(out_folder, d)
    if not os.path.exists(resDir):
        makedirs(resDir)
    for f in listdir(vidDir):       

        img = imread(join(vidDir, f))
        segDir = join(setting, d)
        frameName = str.split(f, '.')[0]
        anno_rgb = imread(segDir + '/' + frameName + '.png').astype(np.uint32)
        labels = np.zeros((2, img.shape[0], img.shape[1]))

        tau=1.05
        EPSILON = 1e-8
        anno_norm = anno_rgb / 255.
        n_energy = -np.log((1.0 - anno_norm + EPSILON)) / (tau * sigmoid(1 - anno_norm))
        p_energy = -np.log(anno_norm + EPSILON) / (tau * sigmoid(anno_norm))
        labels[1, :, :] = n_energy
        labels[0, :, :] = p_energy

        colors = [0, 255]
        colorize = np.empty((len(colors), 1), np.uint8)
        colorize[:,0] = colors

        n_labels = 2

        crf = dcrf.DenseCRF(img.shape[1] * img.shape[0], n_labels)

        U = unary_from_softmax(labels)
        crf.setUnaryEnergy(U)

        feats = create_pairwise_gaussian(sdims=(3, 3), shape=img.shape[:2])

        crf.addPairwiseEnergy(feats, compat=3,
                        kernel=dcrf.DIAG_KERNEL,
                        normalization=dcrf.NORMALIZE_SYMMETRIC)

        feats = create_pairwise_bilateral(sdims=(30, 30), schan=(5, 5, 5),
                                      img=img, chdim=2)
        crf.addPairwiseEnergy(feats, compat=5,
                        kernel=dcrf.DIAG_KERNEL,
                        normalization=dcrf.NORMALIZE_SYMMETRIC)

        Q, tmp1, tmp2 = crf.startInference()
        
        for i in range(10):
            temp = crf.klDivergence(Q)
            crf.stepInference(Q, tmp1, tmp2)        
            if abs(crf.klDivergence(Q)-temp) < 500:
                break
        
        MAP = np.argmax(Q, axis=0)
        MAP = colorize[MAP]
        imsave(resDir + '/' + frameName + '.png', MAP.reshape(anno_rgb.shape))
        print(resDir + '/' + frameName + '.png')
        
print("Done.")