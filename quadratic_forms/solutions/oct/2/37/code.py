# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1acHvh-ADUrjhEpkhJPlOZccQFKL0XLDX
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
#For the first parabola
m=np.reshape([1,0],(2,1))
#print(m)
V1=np.reshape([1,0,0,0],(2,2))
#print(V)
u1=np.reshape([0,-2],(2,1))
f1=0
q1=np.reshape([0,4],(2,1))
q2 = np.reshape([0,0],(2,1))

mu11 = (-m.T@(V1@q1+u1)+ np.sqrt((m.T@(V1@q1+u1))**2-(q1.T@V1@q1+2*u1.T@q1+f1)*(m.T@V1@m)))/((m.T)@V1@m)
mu12 = (-m.T@(V1@q1+u1)- np.sqrt((m.T@(V1@q1+u1))**2-(q1.T@V1@q1+2*u1.T@q1+f1)*(m.T@V1@m)))/((m.T)@V1@m)

M1 = q1 + mu11*m

print("M1 = ",q1 + mu11*m)
print("P1 = ",q1 + mu12*m)

mu13 = (-m.T@(V1@q2+u1)+ np.sqrt((m.T@(V1@q2+u1))**2-(q2.T@V1@q2+2*u1.T@q2+f1)*(m.T@V1@m)))/((m.T)@V1@m)
print("K1 = ",q2 + mu13*m)

#For 2nd parabola
m1=np.reshape([0,1],(2,1))
V2=np.reshape([0,0,0,1],(2,2))
u2=np.reshape([-2,0],(2,1))
f2=0
q11=np.reshape([4,0],(2,1))
q21 = np.reshape([0,0],(2,1))
mu21 = (-m1.T@(V2@q11+u2)+ np.sqrt((m1.T@(V2@q11+u2))**2-(q11.T@V2@q11+2*u2.T@q11+f2)*(m1.T@V2@m1)))/((m1.T)@V2@m1)
mu22 = (-m1.T@(V2@q21+u2)+ np.sqrt((m1.T@(V2@q21+u2))**2-(q21.T@V2@q21+2*u2.T@q21+f2)*(m1.T@V2@m1)))/((m1.T)@V2@m1)
print("M2 = ",q11 + mu21*m1)
print("K2 = ",q21 + mu22*m1)
eta = -0.5

#final intersections
M = q11 + mu21*m1
K = q21 + mu22*m1

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

#x^2 = 4y using affine transformations
len = 1000
x1 = np.linspace(-6,6,len)
D_vec1, P1 = linalg.eig(V1)

D1 = np.diag(D_vec1)
eta1 = u1.T@P1[:,1]
foc1 = -(2*eta)/D_vec1[0]
x_para = (x1**2/foc1)/4
xStandardparab = np.vstack((x1,x_para))

#y^2 = 4ax using affine transformations
y=np.linspace(-6,6,len)
D_vec2,P2 = linalg.eig(V2)

D2 = np.diag(D_vec2)
eta2 = u2.T@P2[:,0]
foc2 = -(2*eta)/D_vec2[1]
y_para = (y**2/foc2)/4
yStandardparab = np.vstack((y_para,y))

#coordinates of each point
l = np.array([4,0])
k = np.array([0,0])
m=np.array([4,4])
n=np.array([0,4])

#plotting points
plt.plot(m[0], m[1], 'o',color='b')
plt.text(m[0] + 0.3, m[1] + 0.3, 'M')
plt.plot(n[0], n[1], 'o',color='orange')
plt.text(n[0] + 0.3, n[1] +0.3, 'N')
plt.plot(l[0], l[1], 'o')
plt.text(l[0] + 0.3, l[1] + 0.3, 'L')
plt.plot(k[0], k[1], 'o')
plt.text(k[0] - 0.8, k[1] + 0.3, 'K')


#Plotting all lines
plt.axhline(y=0,color='yellow',label = 'y=$0$' ,linestyle='--')
plt.axvline(x=4,color='blue',label = 'x=$4$' ,linestyle='--')
plt.axhline(y=4,color='yellow',label = 'y=$4$' ,linestyle='--')
plt.axvline(x=0,color='blue',label = 'x=$0$' ,linestyle='--')

#Plotting the actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='x^2 = 4y',color='r')
plt.plot(yStandardparab[0,:],yStandardparab[1,:],label='y^2 = 4x',color='g')
plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()