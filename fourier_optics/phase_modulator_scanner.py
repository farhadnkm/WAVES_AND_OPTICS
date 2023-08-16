import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')

wl = 0.5
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
xx, yy = np.meshgrid(x, y)
rr2 = xx*xx + yy*yy
f = 10

phi = rr2 / (2*wl*f)

t = np.exp(2j * np.pi * phi)

plt.imshow(phi)
plt.show()

plt.imshow(np.angle(t), cmap='inferno')
plt.show()
