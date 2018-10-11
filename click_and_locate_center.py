import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imshow, bytescale, imsave
import os, glob, h5py, cv2
from operator import itemgetter

patch_size = 50  # square size
imgs = glob.glob('*.png') # get names of all images with .png extension
imgs += glob.glob('*.jpg') # add to that names of all images with .jpg extension
num_imgs = len(imgs)  # number of images to load in


def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    global coords
    coords.append((ix, iy))
    if ix > 2000 and iy > 1500:
        fig.canvas.mpl_disconnect(cid)
        plt.close(1)
    return


for img_num, img in enumerate(imgs):
    # make sure not to do ones you've already done if running twice in same place
    if 'img+target' in img:
        continue

    img = bytescale(imread(img))  # read in each image one at a time

    # if img is RGBA format, get rid of A
    if img.shape[-1] == 4:
        img = img[..., :3]

    coords = []  # where the coordinates will go

    # show the image and allow mouse clicks
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(np.uint8(img))
    fig.set_size_inches(100, 100)

    # get mouse click locations
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    # if accidentally clicked outside image, forget that one
    try:
        coords = np.int32(np.floor(coords))
    except AttributeError:
        continue

    for coord_num, coord in enumerate(coords):
        output = np.zeros(img.shape)

        try:
            output[coord[1]-patch_size//2:coord[1]+patch_size//2, coord[0]-patch_size//2:coord[0]+patch_size//2, :] = 255
        except IndexError:
            continue

        # put the input and target together
        output = np.concatenate((img, output), 1)
        print(output.shape)
        imsave('img+target_' + imgs[img_num][:-4] + '.jpg', output)
