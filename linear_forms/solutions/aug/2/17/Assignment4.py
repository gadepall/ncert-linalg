import numpy as np
import matplotlib.pyplot as plt
from numpy import exp
from matplotlib.pylab import rcParams 
t1 = np.linspace(0.75,2.5 ,10)
t2 = np.linspace(0.75,2.5 ,10)
x1 = 3*t1 - 3
x2 = -(t2/3)+(13/9)
A = np.array([1,0])
B = np.array([2,3])
C = np.array([4/3,1])
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.2), A[1] * (1 + 0.2)+0.2 , 'A(1,0)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.1), B[1] * (1 + 0.1) , 'B(2,3)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 - 0.2), C[1] * (1 + 0.2) , 'C(4/3,1)')
plt.plot(t1,x1,color= 'b', label = 'given line')
plt.plot(t2,x2,color = 'r',label = 'perpendicular line')
rcParams['figure.figsize']=3,7.5
plt.xlabel('X - axis')
plt.ylabel('Y - axis')
plt.grid()
plt.legend(loc='best')
plt.show()
