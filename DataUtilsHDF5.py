import h5py
import numpy as np
from glob import glob
from secrets import choice
import os


def groupH5(path):
    output_file = h5py.File('RoverData.h5', 'a')
    filenames = glob(os.path.join(path, '*.h5'))

    for idx, filename in enumerate(filenames):
        group = output_file.create_group('DataFile_{}'.format(idx))
        X_loc = group.create_group('data')
        Y_loc = group.create_group('labels')

        X_loc['data'] = h5py.ExternalLink(filename, 'X')
        Y_loc['labels'] = h5py.ExternalLink(filename, 'Y')

    output_file.close()
