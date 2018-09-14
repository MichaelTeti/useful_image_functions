def whiten(imgs):
    '''Whitens a NxHxW tensor of images called imgs using a
       fourier decomposition.'''

    imgs -= np.mean(imgs, 0)
    imgs_fft = fft(fft(imgs, axis=1), axis=2)
    spectrum = np.sqrt(np.mean(np.absolute(imgs_fft) ** 2))
    white = ifft(ifft(imgs_fft * (1. / spectrum), axis=1), axis=2)

    return white
