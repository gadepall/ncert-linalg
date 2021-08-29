# -*- coding: utf-8 -*-
"""assignmnt12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mj4xV0o2yMZ5eCQk6xb8YvxWNl9Kzkkg
"""

# -*- coding: utf-8 -*-
"""Assignment-12(1).ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1uWix_ThZqrBlRZNrbg7berH8ZKPHw_0A
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
 
#Generating and plotting line x+y =1200
A=np.array([0,1200])
B=np.array([1200,0])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='x+y= 1200')
 
#Generating and plotting line 2y-x = 0
C=np.array([0,0])
D=np.array([1000,500])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:],label='x-2y=0')
 
 #Generating and plotting line x-3y = 600
E=np.array([0,-200])
F=np.array([1350,250])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='x-3y=600')

 
 
#Shading Required Region
x1=[800,1050,600,0]
y1=[400,150,0,0]
plt.fill(x1,y1)
 
#Labelling points
plt.plot(600,0,'o',color='r')
plt.text(600,0,'A(600,0)')
plt.plot(1050,150,'o',color='r')
plt.text(1050,150,'B(1050,150)')
plt.plot(800,400,'o',color='r')
plt.text(800,400,'C(800,400)')


 
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')