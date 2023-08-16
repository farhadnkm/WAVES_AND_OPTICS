import numpy as np
from numpy.fft import fftshift, fft2, ifft2
from skimage import data

import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')


image = np.array(data.camera()).astype(np.float64)
plt.imshow(image)
plt.show()


image_f = fftshift(fft2(image))
plt.imshow(np.log(np.abs(image_f)))
plt.show()


Ny, Nx = image.shape
x = np.linspace(-10, 10, Nx)
y = np.linspace(-10, 10, Ny)
xx, yy = np.meshgrid(x, y)
rr2 = xx*xx + yy*yy


R = 1
aperture_lp = np.zeros_like(image)
aperture_lp[rr2 < R*R] = 1

image_f_lp = aperture_lp * image_f
plt.imshow(np.log(np.abs(image_f_lp)+0.0001))
plt.show()

image_lp = ifft2(image_f_lp)
plt.imshow(np.abs(image_lp))
plt.show()



R = 2
aperture_lp = np.zeros_like(image)
aperture_lp[rr2 > R*R] = 1

image_f_hp = aperture_lp * image_f
plt.imshow(np.log(np.abs(image_f_hp)+0.0001))
plt.show()

image_hp = ifft2(image_f_hp)
plt.imshow(np.abs(image_hp))
plt.show()





R1 = 1
R2 = 2
aperture_lp = np.zeros_like(image)
aperture_lp[np.logical_and(rr2 > R1*R1, rr2 < R2*R2)] = 1

image_f_hp = aperture_lp * image_f
plt.imshow(np.log(np.abs(image_f_hp)+0.0001))
plt.show()

image_hp = ifft2(image_f_hp)
plt.imshow(np.abs(image_hp))
plt.show()




stripes = np.zeros_like(image)
stripes[::8, :] = 1
stripes[:, ::8] = 1
stripes[rr2 > 64] = 0
plt.imshow(stripes)
plt.show()

image_f = fftshift(fft2(stripes))
plt.imshow(np.log(np.abs(image_f)))
plt.show()

D = 1
aperture_lp = np.zeros_like(stripes)
aperture_lp[np.logical_and(xx > -D/2, xx < D/2)] = 1

image_f_hp = aperture_lp * image_f
plt.imshow(np.log(np.abs(image_f_hp)+0.0001))
plt.show()

image_hp = ifft2(image_f_hp)
plt.imshow(np.abs(image_hp))
plt.show()
