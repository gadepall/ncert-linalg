import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

len = 500

#Standard parabola
y1 = np.linspace(-3,3,len)
y2 = np.power(y1,2)
y = np.vstack((y1,y2))

#Given parabola parameters
V = np.array(([1,0],[0,0]))
u = np.array([0,0])
F = 2

#Affine transformation
g = -np.array([0,1])
vcm = g-u
vcp = g+u
A = np.vstack((V,vcp.T))
b = np.append(vcm,-F)
c = LA.lstsq(A,b,rcond=None)[0]
c = c.reshape(2,1)

#Generating the parabola
x_par = y + c

#plotting the parabola
plt.plot(x_par[0,:],x_par[1,:],label='$x^2 + 2$')

#Plotting all points
plt.plot(c[0], c[1], 'o')
plt.text(c[0] * (1 + 0.1), c[1] * (1-0.1) , '$(0,2)$')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()
