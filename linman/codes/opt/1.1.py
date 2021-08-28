#Code by GVV Sharma
#December 25, 2019
#Released under GNU GPL
#Convex function

import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

#Plotting log(x)
x = np.linspace(1,8,50)#points on the x axis
f=np.log(x)#Objective function
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$\ln x$')

#Convexity/Concavity
a = 2
b = 7
lamda = 0.4
c = lamda *a + (1-lamda)*b
f_a = np.log(a)
f_b = np.log(b)

f_c = np.log(c)
f_c_hat = lamda *f_a + (1-lamda)*f_b

#Plot commands
plt.plot([a,a],[0,f_a],color=(1,0,0),marker='o',label="$f(a)$")
plt.plot([b,b],[0,f_b],color=(0,1,0),marker='o',label="$f(b)$")
plt.plot([c,c],[0,f_c],color=(0,0,1),marker='o',label="$f(\lambda a + (1-\lambda)b)$")
plt.plot([c,c],[0,f_c_hat],color=(1/2,2/3,3/4),marker='o',label="$\lambda f(a) + (1-\lambda)f(b)$")
plt.plot([a,b],[f_a,f_b],color=(0,1,1))
plt.legend(loc=2)
#plt.savefig('../figs/1.1.pdf')
#subprocess.run(shlex.split("termux-open ../figs/1.1.pdf"))
##plt.show()#Reveals the plot
#if using termux
plt.savefig('./line/figs/convex.pdf')
plt.savefig('./line/figs/convex.eps')
subprocess.run(shlex.split("termux-open ./line/figs/convex.pdf"))
#else
#plt.show()












