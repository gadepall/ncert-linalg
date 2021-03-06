# -*- coding: utf-8 -*-
"""a6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ut1Ski_GGXUat6IQfGHrHzpJ2brCuYam
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


O = np.array(([-1,0])) # found from eq
f = 0  # solved from equation
a=2
b=2
q1=np.array(([-1,2]))
q2=np.array(([-1,-2]))


# function to generate circle
def ellipse_gen(a,b):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_ellipse = np.zeros((2,len))
	x_ellipse[0,:] = a*np.cos(theta)
	x_ellipse[1,:] = b*np.sin(theta)
	x_ellipse = (x_ellipse.T + O).T
	return x_ellipse
   

##Generating the circle
x_ellipse= ellipse_gen(a,b)
plt.plot(x_ellipse[0,:],x_ellipse[1,:],label='$ellipse$')
plt.axhline(y=q1[1],color='r',label='$tangent1$')
plt.axhline(y=q2[1],color='r',label='$tangent2$')

#plotting and labelling of points
plt.plot(q1[0], q1[1], '.')
plt.text(q1[0] * (1 + 0.1), q1[1] * (1 + 0.1) , 'Q1(-1,2)')
plt.plot(q2[0], q2[1], '.')
plt.text(q2[0] * (1 -0.06), q2[1] * (1+0.05) , 'Q2(-1,-2)')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.savefig('ellipse.png')
plt.show()