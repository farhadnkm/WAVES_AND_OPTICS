import numpy as np
from numpy.fft import fftshift, fft2
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')


h = 20
w = 10
Nx, Ny = (256, 256)

x = np.linspace(-10, 10, Nx)
y = np.linspace(-10, 10, Ny)
xx, yy = np.meshgrid(x, y)

Dx = 1
Dy = 2

aperture = np.zeros((Ny, Nx))
aperture[np.logical_and(np.abs(xx) < Dx/2, np.abs(yy) < Dy/2)] = 1

diffraction = fftshift(fft2(aperture))

plt.imshow(aperture, cmap='inferno')
plt.show()
plt.imshow(np.abs(diffraction)**2, cmap='inferno')
plt.show()

plt.plot((np.abs(diffraction)**2)[Ny//2, :], label='I(x,0)')
plt.plot((np.abs(diffraction)**2)[:, Nx//2], label='I(0,y)')
plt.legend()
plt.show()




rr = np.sqrt(xx*xx + yy*yy)
D = 0.7

aperture = np.zeros((Ny, Nx))
aperture[rr < D] = 1

diffraction = fftshift(fft2(aperture))

plt.imshow(aperture, cmap='inferno')
plt.show()
plt.imshow(np.abs(diffraction)**1, cmap='inferno')
plt.show()

plt.plot((np.abs(diffraction)**2)[Ny//2, :])
plt.show()