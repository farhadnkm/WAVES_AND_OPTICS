import numpy as np



def E_field(q, x0, y0, x, y):
    x_ = x - x0
    y_ = y - y0
    r2 = x_*x_ + y_*y_
    return np.stack([q*x_/np.power(r2, 1.5), q*y_/np.power(r2, 1.5)], axis=0)



def divergence2D(fx, fy, dx, dy):
    fxx1  = np.copy(fx)
    fxx_1 = np.copy(fx)
    fyy1  = np.copy(fy)
    fyy_1 = np.copy(fy)
    
    fxx1[:, :-1] = fx[:,  1:]
    fxx_1[:, 1:] = fx[:, :-1]
    fyy1[:-1, :] = fy[1:,  :]
    fyy_1[1:, :] = fy[:-1, :]

    dfxx = (fxx1 - fxx_1)/(2*dx)
    dfyy = (fyy1 - fyy_1)/(2*dy)
    return dfxx + dfyy




def curl(fx, fy, fz, dx, dy, dz):
    fxy1  = np.copy(fx)
    fxy_1 = np.copy(fx)
    fxz1  = np.copy(fx)
    fxz_1 = np.copy(fx)
    fyx1  = np.copy(fy)
    fyx_1 = np.copy(fy)
    fyz1  = np.copy(fy)
    fyz_1 = np.copy(fy)
    fzx1  = np.copy(fz)
    fzx_1 = np.copy(fz)
    fzy1  = np.copy(fz)
    fzy_1 = np.copy(fz)
    
    fxy1[:-1,  ...] = fx[1:,   ...]
    fxy_1[1:,  ...] = fx[:-1,  ...]
    fxz1[...,  :-1] = fx[...,   1:]
    fxz_1[...,  1:] = fx[...,  :-1]

    fyx1[:, :-1, :] = fy[:,  1:, :]
    fyx_1[:, 1:, :] = fy[:, :-1, :]
    fyz1[...,  :-1] = fy[...,   1:]
    fyz_1[...,  1:] = fy[...,  :-1]

    fzx1[:, :-1, :] = fz[:,  1:, :]
    fzx_1[:, 1:, :] = fz[:, :-1, :]
    fzy1[:-1,  ...] = fz[1:,   ...]
    fzy_1[1:,  ...] = fz[:-1,  ...]

    dfxy = (fxy1 - fxy_1)/(2*dy)
    dfxz = (fxz1 - fxz_1)/(2*dz)
    dfyx = (fyx1 - fyx_1)/(2*dy)
    dfyz = (fyz1 - fyz_1)/(2*dz)
    dfzx = (fzx1 - fzx_1)/(2*dx)
    dfzy = (fzy1 - fzy_1)/(2*dy)

    return dfzy - dfyz, dfxz - dfzx, dfyx - dfxy
