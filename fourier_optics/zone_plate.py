import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')

wl = 0.5
x = np.linspace(-100, 100, 1000)
y = np.linspace(-100, 100, 1000)
xx, yy = np.meshgrid(x, y)
rr2 = xx*xx + yy*yy
f = 1000

phi = rr2 / (2*wl*f)

t = np.cos(2 * np.pi * phi)
t = np.where(t > 0, 1, 0)


plt.imshow(phi)
plt.show()

plt.imshow(t, cmap='inferno')
plt.show()
