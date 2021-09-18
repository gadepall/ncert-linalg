from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#from coeffs import *
import numpy as np

#if using termux

#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid([-15,15], range(15))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#defining lines : x(k) = A + k*l

#defining planes:  n.T * x = c 
n1 = np.array([1,1,1]).T
n2 = np.array([2,3,-1]).T

d1=1
d2=-4

#corresponding z for planes
z1 = (d1-n1[0]*xx-n1[1]*yy)/(n1[2])
z2 = (d2-n2[0]*xx-n2[1]*yy)/(n2[2])


#plotting planes
Plane=ax.plot_surface(xx, yy, z1,label="x+y+z=1", color='r',alpha=0.5)
Plane._facecolors2d=Plane._facecolor3d
Plane._edgecolors2d=Plane._edgecolor3d

Plane=ax.plot_surface(xx, yy, z2,label="2x+3y-z=-4", color='b',alpha=0.5)
Plane._facecolors2d=Plane._facecolor3d
Plane._edgecolors2d=Plane._edgecolor3d

n=np.cross(n1,n2)
n=np.cross(np.array([1,0,0]).T,n)
k=6

z = (k-n[0]*xx-n[1]*yy)/(n[2])
Plane=ax.plot_surface(xx, yy, z,label="-y+3z=6", color='g',alpha=0.5)
Plane._facecolors2d=Plane._facecolor3d
Plane._edgecolors2d=Plane._edgecolor3d



#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()
