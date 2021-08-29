from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#creating x,y for 3D plotting
zz, xx = np.meshgrid(range(-20,20), range(-20,20))


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Points
A = np.array([5,1,6]).reshape((3,1))
B = np.array([17/3,0,23/3]).reshape((3,1))
C=np.array([3,4,1]).reshape((3,1))
#Generating all lines
x_BC = line_gen(C,B)
#plotting line
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],color='g')
 
#corresponding z for planes
yy=0*xx
#plotting planes
Plane1=ax.plot_surface(xx,yy,zz, color='b',alpha=0.25,label='YZ Plane ')
Plane1._facecolors2d=Plane1._facecolor3d
Plane1._edgecolors2d=Plane1._edgecolor3d

#Plotting and labelling point A

ax.scatter(5,1,6,'o')
ax.text(5 * (1 + 0.1), 1 * (1 - 0.1) ,6*(1-0.1), "(5,1,6)")
ax.scatter(17/3,0,23/3,'o')
ax.text((17/3) * (1 + 0.1), 0 * (1 - 0.1) ,(23/3)*(1-0.1), "(5.67,0,7.67)")
ax.scatter(3,4,1,'o')
ax.text(3 * (1 + 0.1), 4 * (1 - 0.1) ,1*(1-0.1), "(3,4,1)")

plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.legend()

plt.show()