# -*- coding: utf-8 -*-
"""ASSIGNMENT5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jhWgvwQGhh-RLV6ZKbM1paCZUWeAyQvP
"""

# -*- coding: utf-8 -*-
"""ChallengeProblem4.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1lbW3T9SwCX_NLLaMBe6wEsNRVuVL-SM5
"""

#Code by B.Anusha
#June 23, 2021

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
xx, yy = np.meshgrid(range(10), range(10))


#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

#Points
A = np.array([0,0,0]).reshape((3,1))
B = np.array([1,2,3]).reshape((3,1))

#Generating all lines
x_AB = line_gen(A,B)
#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],color='g',label='OP')

#defining planes:  n.T * x = c 
n1 = np.array([1,2,3]).reshape((3,1))
P =  np.array([1,2,3]).reshape((3,1))
c1 = 14

 
#corresponding z for planes
z1 = (c1-n1[0]*xx-n1[1]*yy)/(n1[2])
 
#plotting planes
Plane1=ax.plot_surface(xx,z1,yy, color='b',alpha=0.25,label='Plane (1 2 3)x=14')
Plane1._facecolors2d=Plane1._facecolors3d
Plane1._edgecolors2d=Plane1._edgecolors3d

#Plotting and labelling point A
ax.scatter(P[0],P[1],P[2],'o')
ax.text(1.2,2.2,3.2,'P')
ax.scatter(1,2,3,'o')
ax.text(-1.1,1.2,1.1, "OP")

plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.legend(loc='best')


plt.show()