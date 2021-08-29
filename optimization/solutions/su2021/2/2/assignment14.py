# -*- coding: utf-8 -*-
"""assignment14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MyrvpCRaLNmx97Wx8mzFNlgRCeo7ey5X
"""

import numpy as np
import matplotlib.pyplot as plt

#Defining f(x)
def f(x,a,b,d):
	return a*(x**2)+b*x+d
a = -18
b = -72
d = 41

#For maxima using gradient ascent
cur_x = 2
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 2*a*x + b           

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  



print("Maximum value of f(x) is ",f(cur_x,a,b,d), "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-4,0,80)
y=-18*(x**2)-72*x+41
plt.plot(x,y,label='41-72x-18x^2$')

#Labelling points
plt.plot(cur_x,f(cur_x,a,b,d),'o')
plt.text(cur_x*(1+0.4), f(cur_x,a,b,d)*(1-0.01),'P(-2,113)')



plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
#if using termux
plt.savefig('assignment14.png')
#else
plt.show()