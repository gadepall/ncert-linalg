from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

xx, yy = np.meshgrid(range(10), range(10))

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
plt.grid()

#Plane points
A1 = np.array([0,0,0])
A2 = np.array([5,2,3])
m1 = np.array([2,2,1])
m2 = np.array([4,1,8])
k1 = -4
k2 = 4
x2_dist_skew = line_dir_pt(m2,A2,k1,k2)
x1_dist_skew = line_dir_pt(m1,A1,k1,k2)

#Plotting all lines
plt.plot(x1_dist_skew[0,:],x1_dist_skew[1,:], x1_dist_skew[2,:],label='$LineEquation-3.0.13$')
plt.plot(x2_dist_skew[0,:],x2_dist_skew[1,:], x2_dist_skew[2,:], label='$LineEquation-3.0.14$')
#plotting points
ax.scatter(A1[0],A1[1],A1[2],'o')
ax.scatter(A2[0],A2[1],A2[2],'o')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.savefig('./figs/Line_interest_2.pdf')
plt.savefig('./figs/Line_interest_2.eps')