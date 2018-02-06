import numpy as np
import os, sys
import glob
from scipy.misc import imread, imresize


def img_reader(dir, imsz, file_ex=None):
    ''' A function that reads in images contained
        in each folder in dir, resizes them to 
        imsz[0] x imsz[1], and attaches a label to 
        each image based on the folder it came from. 
        
        Args:
             dir: directory where the image folders are 
                  located.
             imsz: a list of length 2, where each number 
                   represents the height and width each
                   image will be resized to. If all images 
                   are the same size and don't need to be
                   resized, just put the size they already 
                   are.
              file_ex: if the images you want to compile 
                       are all of the same extension and/or
                       there are other file types in the 
                       folders that you don't want to read,
                       you can include the extension as file_ex.
                       Example, file_ex = '.jpg'
    ''' 
    
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
