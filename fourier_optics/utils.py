import numpy as np


def convolve1d(input_, impulse_response, stride=1):

    n_b = impulse_response.shape[0]
    n_a = input_.shape[0]
    ind = np.arange(0, n_a, stride)
    a_ = np.pad(input_, [n_b // 2, n_b // 2], mode='constant')

    res = np.zeros_like(input_)
    for i in ind:
        res[i] = np.sum(a_[i:i+n_b] * impulse_response)
    return res
