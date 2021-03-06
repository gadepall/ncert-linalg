# -*- coding: utf-8 -*-
"""Assignment-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QLgolGDxpC5slk5p3tlwNVThAIhm096o
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


#if using termux
import subprocess
import shlex
#end if

#creating x,y for 3D plotting
xx, yy = np.meshgrid([-10,10], range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


#defining planes:  n.T * x = c 
n1 = np.array([1,1,-1]).reshape((3,1))
A =  np.array([1,0,-2]).reshape((3,1))
c1 = 3

#corresponding z for planes
z1 = (c1-n1[0]*xx-n1[1]*yy)/(n1[2])

#plotting planes
Plane=ax.plot_surface(xx, yy, z1,label="Plane", color='b',alpha=0.5)
Plane._facecolors2d=Plane._facecolors3d
Plane._edgecolors2d=Plane._edgecolors3d
#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.text(1.2,0.2,-2.2,'A') 

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()