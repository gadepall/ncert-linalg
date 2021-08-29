# -*- coding: utf-8 -*-
"""ChallengeProblem5_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gF9lmKx-VMyp10QEtem0M8t6Tb-sKftL
"""

#Code by K.A. Raja Babu
#June 24,2021

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

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

O=np.array([0,0])
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	x_ellipse = (x_ellipse.T + O).T
	return x_ellipse
   
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)

#Ellipse parameters
V = 1/2*np.array(([1,1/2],[1/2,1]))
u = np.array(([0,0]))
f = -100
c = -LA.inv(V)@u

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
pcos = np.cos(np.pi/4)
psin = np.sin(np.pi/4)
P = np.array(([pcos,-psin],[psin,pcos]))
a = np.sqrt(-f/D_vec[0])
b = np.sqrt(-f/D_vec[1])
xStandardEllipse = ellipse_gen(a,b)

#Major and Minor Axes
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

#Affine transform 
xActualEllipse = P@xStandardEllipse
MajorActual = P@MajorStandard
MinorActual = P@MinorStandard

#Plotting the actual ellipse
plt.plot(xActualEllipse[0,:],xActualEllipse[1,:],label='$x^2$+xy+$y^2$=100')

#Plotting minor axis
R=np.array([15,15])
S=np.array([-15,-15])
RS=line_gen(R,S)
plt.plot(RS[0,:],RS[1,:],'--',label='(-1 1)x=0')

#Plotting major axis
R1=np.array([-15,15])
S1=np.array([15,-15])
RS1=line_gen(R1,S1)
plt.plot(RS1[0,:],RS1[1,:],'--',label='(1 1)x=0')

plt.plot(0,0,'o',color='r')
plt.text(1.8,0.5,'c')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()