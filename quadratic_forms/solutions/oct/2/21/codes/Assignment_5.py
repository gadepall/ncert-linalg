import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from sympy import *
x = np.arange(-5,5,0.0001)
y1 = (3*(x**2))-(5*x)+2
plt.plot(x,y1)
plt.grid()
plt.show()
x = np.arange(-8,5,0.0001)
y2 = (x**2) + (4*x) + 5
plt.plot(x,y2,color='y')
 
plt.grid()
plt.show()
x = np.arange(-5,8,0.0001)
y3 = (2*(x**2))-(np.sqrt(2)*2*x)+1
plt.plot(x,y3,color='r')
plt.grid()
plt.show()
