import numpy as np
import matplotlib.pyplot as plt
import os, glob, h5py, cv2
from operator import itemgetter

patch_size = 500  # square size
imgs = glob.glob('*.png') # get names of all images with .png extension
imgs += glob.glob('*.jpg') # add to that names of all images with .jpg extension
num_imgs = len(imgs)  # number of images to load in
change = False



def click(event, x, y, flags, param):
	# grab references to the global variables
    global coords

    # if mouse click, record coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        coords = [x, y]
        cv2.destroyAllWindows()


# loop through each image in the directory, show it, and get coordinates
for img_num, img in enumerate(imgs):
    img_read = cv2.imread(img)  # read in each image one at a time
    mask = np.int32(np.zeros(img_read.shape))  # create a black mask

    # if img is RGBA format, get rid of A
    if img_read.shape[-1] == 4:
        img_read = img_read[..., :3]

    # resize image to show it
    img_resized = cv2.resize(img_read, (img_read.shape[1]//3, img_read.shape[0]//3, ))

    # show image and get key presses
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click)
    cv2.imshow("image", img_resized)
    key = cv2.waitKey(15000) & 0xFF

    x, y = coords
    x *= 3
    y *= 3
    mask[y-patch_size//2:y+patch_size//2, x-patch_size//2:x+patch_size//2, :] = 255
    img_target = np.concatenate((img_read, mask), 1)

    if 'images_and_targets' not in os.listdir():
        os.mkdir('images_and_targets')

    # save the image
    cv2.imwrite('images_and_targets/' + img, img_target)
