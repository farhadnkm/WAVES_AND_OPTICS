import numpy as np

def E_field(q, x0, y0, x, y):
    x_ = x - x0
    y_ = y - y0
    r2 = x_*x_ + y_*y_
    return np.stack([q*x_/np.power(r2, 1.5), q*y_/np.power(r2, 1.5)], axis=0)