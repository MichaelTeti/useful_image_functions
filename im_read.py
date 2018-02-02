import numpy as np
import os, sys
import glob
from scipy.misc import imread, imresize


def img_reader(dir, imsz, file_ex=None):
    ''' A function to read images in folders
        located in dir, resize them to 
        imsz[0] x imsz[1]. If file_ex is 
        given, it will only compile files of
        type file_ex. Returns the images in 
        NHWC format and the labels. '''

    if file_ex is None:
        file_ex = '*'
    else:
        file_ex = '*' + file_ex

    folders = os.listdir(dir)
    imgs = np.zeros([0, imsz[0], imsz[1], 3])
    labels = np.zeros([0, 1])
    os.chdir(dir)

    for folder in xrange(len(folders)):
        os.chdir(dir + '/' + folders[folder])
        files = glob.glob(file_ex)
        imgs2 = np.zeros([len(files), imsz[0], imsz[1], 3])
        i = 0

        for file in files:
            if os.path.isfile(file):
                img = imread(file)
                img = imresize(img, [imsz[0], imsz[1]])
                imgs2[i, ...] = img
                i += 1
                
        imgs = np.concatenate((imgs, imgs2), 0)
        labels_new = np.ones([1, 1]) * folder
        labels = np.concatenate((labels, labels_new), 0)

    return imgs, labels
