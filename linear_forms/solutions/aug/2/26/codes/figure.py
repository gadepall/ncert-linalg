import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def line_gen(A,B):
  len =10
  x_AB = np.zeros((3,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

n = np.array([0, 1, 0])

xx, zz = np.meshgrid(range(10), range(10))
yy_plane = 3
yy_ZOX = 0

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

C = np.array([0,3,0]).reshape((3,1))
O = np.array([0,0,0]).reshape((3,1))

OC = line_gen(O,C)

plt.grid()

plt.plot(OC[0,:],OC[1,:],OC[2,:],'--')

Plane=ax.plot_surface(xx,yy_plane,zz,label="Required Plane",color='red',alpha=0.5)
Plane._facecolors2d=Plane._facecolors3d
Plane._edgecolors2d=Plane._edgecolors3d

ZOX=ax.plot_surface(xx,yy_ZOX,zz,label="ZOX-Plane",color='yellow',alpha=0.5)
ZOX._facecolors2d=Plane._facecolors3d
ZOX._edgecolors2d=Plane._edgecolors3d

ax.scatter(O[0],O[1],O[2],'o',color='blue')
ax.scatter(C[0],C[1],C[2],'o',color='blue')
ax.text(-0.7,0,0, "O", color='blue')
ax.text(-0.7,3,0, "C", color='blue')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc='best')
ax.view_init(20,-10)
