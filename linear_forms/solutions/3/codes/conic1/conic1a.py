import numpy as np
import matplotlib.pyplot as plt
import subprocess
import  shlex
y = np.linspace(-3,3,100)
p=np.poly1d([1,0,0])
for i in range(len(y)):
    t=p(y)

A=np.array([0,p(0)])
B=np.array([1,p(1)])
C=np.array([2,p(2)])
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'p(0)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.5), B[1] * (1-0.1) , 'p(1)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1-0.1), C[1] * (1-0.1) , 'p(2)')
plt.plot(y,t,label='$p(y)=y^2$')
plt.xlabel('$y$')
plt.ylabel('$p(y)$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.savefig('./pyfigs/conic1a.eps')
plt.show() 
