import numpy as np
from fourier_optics.utils import convolve1d
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')


length = 1000

# defining the impulse response function
input_ = np.zeros(length)
input_[length//2-50 - 1: length//2+50 - 1] = 1

plt.plot(input_)
plt.show()

# defining the input
imp_resp = np.zeros(1000)
imp_resp[length//2-60 - 1: length//2+80 - 1] = np.linspace(0, 1, 140)
imp_resp /= np.sum(imp_resp)

plt.plot(imp_resp)
plt.show()

# solving the convolution integral
conv = convolve1d(input_, imp_resp, 1)

plt.plot(conv)
plt.show()


# transfer function
transfer_func = np.fft.ifft(imp_resp)


# convolution theorem - solving convolution by fourier transforms
conv = np.fft.fftshift(np.fft.ifft((np.fft.fft(input_) * transfer_func)))

plt.plot(np.abs(conv))
plt.show()

def normalize(x):
    x -= np.min(x)
    return x / np.max(x)

plt.plot(normalize(np.abs(np.fft.fftshift(transfer_func))))
plt.show()
plt.plot(normalize(np.abs(np.fft.fftshift(np.fft.fft(input_)))))
plt.show()
plt.plot(normalize(np.abs(np.fft.fftshift(np.fft.fft(conv)))))
plt.show()