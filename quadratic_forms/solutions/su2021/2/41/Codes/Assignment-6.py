# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZuXwva4BeHTPcq3dwf6DJ-lFmEfYzbEJ
"""

#code by Satya Sangram
#for quadforms 2.41
def hyper_gen(y):
	x = np.sqrt(1+y**2)
	return x
def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-2,2,len)

#hyper parameters
V = 1/2*np.array(([0,1],[1,0]))
u = -3/2*np.array(([0,1]))
f = 2
Vinv = LA.inv(V)
#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)

uconst = u.T@Vinv@u-f
a = np.sqrt(np.abs(uconst/D_vec[0]))
b = np.sqrt(np.abs(uconst/D_vec[1]))

#Generating the Standard Hyperbola
x = hyper_gen(y)
xStandardHyperLeft = np.vstack((-x,y))
xStandardHyperRight = np.vstack((x,y))

#Affine Parameters
c = -Vinv@u

R =  np.array(([0,1],[1,0]))
ParamMatrix = np.array(([a,0],[0,b]))

#Generating the eigen hyperbola
xeigenHyperLeft = R@ParamMatrix@xStandardHyperLeft
xeigenHyperRight = R@ParamMatrix@xStandardHyperRight

#Generating the actual hyperbola
xActualHyperLeft = P@ParamMatrix@R@xStandardHyperLeft+c[:,np.newaxis]
xActualHyperRight = P@ParamMatrix@R@xStandardHyperRight+c[:,np.newaxis]


#Hyperbola vertices
V1old = np.array([1,0])
V2old = -V1old

V1 = P@R@ParamMatrix@V1old+c
V2 = P@R@ParamMatrix@V2old+c


#Tangent Analysis
m = np.array(([1,2]))
n = np.array([-2,1])

kappa = np.sqrt(uconst/(n.T@Vinv@n))
q1=Vinv@(kappa*n-u)
q2=Vinv@(-kappa*n-u)


#Generating the tangents
k1 = 2
k2 = -2
x_AB = line_dir_pt(m,q1,k1,k2)
x_BC = line_dir_pt(m,q2,k1,k2)

#Labeling the coordinates
plt.plot(q1[0],q1[1],'o')
plt.text(q1[0]*1.1,q1[1]*1.1,'p')
plt.plot(q2[0],q2[1],'o')
plt.text(q2[0]*1.1,q2[1]*0.8,'q')

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='Tangent1')
plt.plot(x_BC[0,:],x_BC[1,:],label='Tangent2')

#Plotting the eigen hyperbola
#plt.plot(xeigenHyperLeft[0,:],xeigenHyperLeft[1,:],label='Standard hyperbola',color='b')
#plt.plot(xeigenHyperRight[0,:],xeigenHyperRight[1,:],color='b')

#Plotting the actual hyperbola
plt.plot(xActualHyperLeft[0,:],xActualHyperLeft[1,:],label='Actual hyperbola',color='m')
plt.plot(xActualHyperRight[0,:],xActualHyperRight[1,:],color='m')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


plt.show()