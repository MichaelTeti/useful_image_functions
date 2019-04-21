import numpy as np
import os, sys
import glob
from scipy.misc import imread, imresize, imshow
import cv2



def img_reader(dir, imsz, file_ex=None, sort=False, channel_order='channels_last'):
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

    main_dir = os.path.abspath(dir)

    if file_ex is None:
        file_ex = '*'
    else:
        file_ex = '*' + file_ex

    folders = os.listdir(dir)
    num_ims=sum([len(files) for r, d, files in os.walk(dir)])

    if channel_order == 'channels_first':
        imgs = np.zeros([num_ims, 3, imsz[0], imsz[1]])
    elif channel_order == 'channels_last':
        imgs = np.zeros([num_ims, imsz[0], imsz[1], 3])

    labels = np.zeros([num_ims, 1])
    i = 0

    for folder_num, folder in enumerate(folders):
        files_dir = os.path.join(main_dir, folder)
        files = os.listdir(files_dir)
        if sort:
            files.sort()

        for file_num, file in enumerate(files):
            file = os.path.join(files_dir, file)
            if os.path.isfile(file):
                img = imread(file)
                img = imresize(img, [imsz[0], imsz[1]])
                if channel_order == 'channels_first':
                    img = img.transpose((2, 0, 1))

                imgs[i, ...] = img
                labels[i, 0] = folder_num
                i += 1

    return imgs, labels
