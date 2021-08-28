# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hNS6WG4HX5QBV34A1csmcdRN5ngBvglX
"""

#Code by Satya_Sangram
#22/05/2021
#Figure for Q.No 2.55
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#centre and radius of circles
A=np.array([0,0])
B=np.array([3,0])
r1=3
r2=3


#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],'k')


#Plotting the circles
theta = np.linspace(0,2*np.pi,50)
u=np.array([np.cos(theta),np.sin(theta)])

A1=A.reshape(2,1)
B1=B.reshape(2,1)
C1=A1+r1*u
C2=B1+r2*u

plt.plot(C1[0,:],C1[1,:],label='$circle with center A$')
plt.plot(C2[0,:],C2[1,:],label='$circle with center B$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.plot(0,0,'o')
plt.text(-0.3,0.1,'A')
plt.plot(3,0,'o')
plt.text(3.1,0.1,'B')

#intersection points
C=np.array([1.5,2.59807621])
D=np.array([1.5,-2.59807621])

x_CD=line_gen(C,D)
plt.plot(x_CD[0,:],x_CD[1,:],'k')
plt.plot(C[0],C[1],'o')
plt.text(1.5,C[1]*1.1,'C')
plt.plot(D[0],D[1],'o')
plt.text(1.5,D[1]*1.2,'D')

#forming a rhombus
x_AC=line_gen(A,C)
plt.plot(x_AC[0,:],x_AC[1,:],'k')

x_AD=line_gen(A,D)
plt.plot(x_AD[0,:],x_AD[1,:],'k')

x_BC=line_gen(B,C)
plt.plot(x_BC[0,:],x_BC[1,:],'k')

x_BD=line_gen(B,D)
plt.plot(x_BD[0,:],x_BD[1,:],'k')


plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()