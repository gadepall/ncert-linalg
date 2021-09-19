# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T0WPPf9uyaVRC2_F58KpYC1cpVxgCdrP
"""

#Drawing a RECTANGLE OKAY
import numpy as np
import matplotlib.pyplot as plt


#RECTANGLE vertices
O = np.array([0,0])
K = np.array([7,0])
A = np.array([0,5]) 
Y = np.array([7,5]) 

import numpy as np

#Generating all lines
x_OK = line_gen(O,K)
x_KY = line_gen(K,Y)
x_YA = line_gen(Y,A)
x_OA = line_gen(O,A)



#Plotting all lines
plt.plot(x_OK[0,:],x_OK[1,:],label='$OK$')
plt.plot(x_KA[0,:],x_KA[1,:],label='$KA$')
plt.plot(x_AY[0,:],x_AY[1,:],label='$AY$')
plt.plot(x_OY[0,:],x_OY[1,:],label='$OY$')


plt.xlabel('$x$')
plt.ylabel('$y$')

plt.plot(0,0,'o')
plt.plot(7,0,'o')
plt.plot(0,5,'o')
plt.plot(7,5,'o')

plt.text(0,0,'O(0,0)')
plt.text(7,0,'K(7,0)')
plt.text(0,5,'A(0,5)')
plt.text(7,5,'Y(7,5)')

plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.title('RECTANGLE OKAY')
plt.savefig('RECTANGLE.png')
plt.show