# -*- coding: utf-8 -*-
"""ASSIGNMENT9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ic5FkJmDlRXGYdzMhnJ9xHjEosFXb40E
"""

import numpy as np
import matplotlib.pyplot as plt

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

#Plotting line 2x-y =1
A=np.array([3,5])
B=np.array([-2,-5])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='2x-y=1')

#Plotting line x-2y=-1
P=np.array([9,5])
Q=np.array([-5,-2])
PQ=line_gen(P,Q)
plt.plot(PQ[0,:],PQ[1,:],label='x-2y=-1')

#Shading Required Region
x1=[1,3,9]
y1=[1,5,5]
plt.fill(x1,y1,color='green',alpha=0.3)

#Labelling points
plt.plot(1,1,'o',color='r')
plt.text(1.2,1.3,'A(1,1)')


plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()