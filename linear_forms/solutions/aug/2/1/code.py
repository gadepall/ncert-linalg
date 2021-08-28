import numpy as np
import matplotlib.pyplot as plt

plt.axis([4,8,4,8])

plt.axis('on')


#if using termux
import subprocess
import shlex
#end if

# import the math module 
import math 
  
# print the square root of 0
print(math.sqrt(0)) 

#Inputs
n = np.array([1,-2]) 
c = 4

e1 = np.array([0,2]) 
e2 = np.array([4,0]) 
e3 = np.array([2,0]) 
e4 = np.array([np.sqrt(2),4*np.sqrt(2)]) 
e5 = np.array([1,1]) 

A = c*e1/(n@e1)
B = c*e2/(n@e2)
C = c*e3/(n@e3)
D = c*e4/(n@e4)
E = c*e5/(n@e5)


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(0,2,'o')
plt.plot(4,0,'o')
plt.plot(2,0,'o')
plt.plot(1.4,5.65,'o')
plt.plot(1,1,'o')


plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')


plt.text(0,2, 'A(0,2)')
plt.text(4,0, 'B(4,0)')
plt.text(2,0, 'C(2,0)')
plt.text(1.4,5.65, 'D(1.4,5.65)')
plt.text(1,1, 'E(1,1)')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
