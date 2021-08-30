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
zz, yy = np.meshgrid(range(-20,20), range(-20,20))


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Points
A = np.array([5,1,6]).reshape((3,1))
B = np.array([0,17/2,-13/2]).reshape((3,1))
C=np.array([3,4,1]).reshape((3,1))
#Generating all lines
x_AB = line_gen(A,B)
#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],color='g')
 
#corresponding z for planes
xx=0*yy
#plotting planes
Plane1=ax.plot_surface(xx,zz,yy, color='b',alpha=0.25,label='YZ Plane ')
Plane1._facecolors2d=Plane1._facecolors3d
Plane1._edgecolors2d=Plane1._edgecolors3d

#Plotting and labelling point A

ax.scatter(5,1,6,'o')
ax.text(5 * (1 + 0.1), 1 * (1 - 0.1) ,6*(1-0.1), "(5,1,6)")
ax.scatter(0,8.5,-6.5,'o')
ax.text(0 * (1 + 0.1), 8.5 * (1 - 0.1) ,-6.5*(1-0.1), "(0,8.5,-6.5)")
ax.scatter(3,4,1,'o')
ax.text(3 * (1 + 0.1), 4 * (1 - 0.1) ,1*(1-0.1), "(3,4,1)")

#drawVertix(A,"(5,1,6)")
#drawVertix(B,"(0,8.5,-6.5)")
#drawVertix(C,"(3,4,1)")

plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.legend(loc='best')


plt.show()