# -*- coding: utf-8 -*-
"""a5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zJcJBGaWzu6cP1k48AfbXj8bvQZ7m9yL
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

plt.axis([-2,3,0,4])

plt.axis('on')
plt.grid(True)


A = np.array([2,1]) 
#input point B on line AB, to help generate line AB representing given equation
B = np.array([-1,3])


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

  #Generating all lines
x_AB = line_gen(A,B)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$line representing equation$')
plt.plot(2,1,'hm')
plt.text(2,1,'A (2,1)')


plt.savefig('line.pdf')
plt.show()