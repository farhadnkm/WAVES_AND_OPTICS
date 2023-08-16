import numpy as np

N = 100000000

x = np.random.rand(N)
y = np.random.rand(N)
r = np.sqrt(x*x + y*y)

r_ = r[r<= 1]

pi = 4 * len(r_) / N 
print("Estimated value of pi:", pi)


from matplotlib import pyplot as plt

hist_, x_ = np.histogram(r, 1000)
plt.axline((1.0, 0), (1.0, 1), color="orange", linestyle='--')
plt.plot(x_[:-1], hist_)
plt.show()



condition = r <= 1
x_frac = x[::int(N / 10000)]
y_frac = y[::int(N / 10000)]
cond_frac = condition[::int(N / 10000)]
plt.scatter(x_frac[cond_frac], y_frac[cond_frac], 1.0, color='orange')
plt.scatter(x_frac[np.logical_not(cond_frac)], y_frac[np.logical_not(cond_frac)], 1.0, color='green')
plt.show()


# area of a section of a unit circle
theta = np.arcsin(y/r)
condition = np.logical_and(theta < np.pi/3, theta > np.pi/6)
condition = np.logical_and(condition, r <= 1)

print("Estimated area of the shape:", len(r[condition])/N)

cond_frac = condition[::int(N / 10000)]
plt.scatter(x_frac[cond_frac], y_frac[cond_frac], 1.0, color='orange')
plt.scatter(x_frac[np.logical_not(cond_frac)], y_frac[np.logical_not(cond_frac)], 1.0, color='green')
plt.show()