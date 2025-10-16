import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define your function f(x, y)
def f(x, y):
    a1 = (x ** 2) * (x - 6)
    a2 = (y ** 2) * (y - 6)
    a3 = a1 * a2 / 90
    a4 = 85 - a3
    return a4

mypath = ".\\images\\"
myfilename = "3D_plot.png"

# Define the grid
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)

# Evaluate the function on the grid
Z = f(X, Y)
#Z = f(X, Y) + g(X, Y)

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.9)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z = f(x, y)')
ax.set_title('3D Surface of f(x, y)')

# save plot to file
plt.savefig(f"{mypath}{myfilename}", dpi=300, bbox_inches='tight')
plt.close()
