from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs import *

# This function use least square to find minimum between lines
def distance_between_skew_lines(A,B):
    
    inverse = np.linalg.inv(A.T @ A)
    x = (inverse @ A.T) @ B

    # Calculate distance
    d = np.linalg.norm((A @ x) - B)
    return d


# Plane points
A1 = np.array([-1, -1, -1])
A2 = np.array([3, 5, 7])
m1 = np.array([7, -6, 1])
m2 = np.array([1, -2, 1])
# m1, m2 = Direction vector
# A1, A2 = Point where the line passes through

A = np.concatenate((m1, m2)).reshape(2, 3).T
B = A1-A2

print("Shortest distance between given skew lines :",
      distance_between_skew_lines(A, B))

print("Verifying using inbuilt function :", np.linalg.norm(
    (A @ np.linalg.lstsq(A, B, rcond=None)[0]) - B))

'''
# Output
Shortest distance between given skew lines : 10.77032961426901
Verifying using inbuilt function : 10.770329614269007
'''

# creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
# setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

k1 = -4
k2 = 4
x2_dist_skew = line_dir_pt(m2, A2, k1, k2)
x1_dist_skew = line_dir_pt(m1, A1, k1, k2)

# Plotting all lines
plt.plot(x1_dist_skew[0, :], x1_dist_skew[1, :],
         x1_dist_skew[2, :], label='$L_1$')
plt.plot(x2_dist_skew[0, :], x2_dist_skew[1, :],
         x2_dist_skew[2, :], label='$L_2$')
# plotting points
ax.scatter(A1[0], A1[1], A1[2], 'o')
ax.scatter(A2[0], A2[1], A2[2], 'o')
ax.text(-1, -1, -1, "A1", color='red')
ax.text(3, 5, 7, "A2", color='green')

# Plotting
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
