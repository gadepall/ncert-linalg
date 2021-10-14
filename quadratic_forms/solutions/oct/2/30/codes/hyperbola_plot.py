import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111)
len = 500
y = np.linspace(-10,10,len)

def hyperbola_gen(y):
	x = np.sqrt((100*(y**2)-275)/44)
	return x

#Generating the Standard Hyperbola
x = hyperbola_gen(y)
xStandardLeft = np.vstack((-x,y))
xStandardRight = np.vstack((x,y))

#Plotting points
A = np.array([0,3])
B = np.array([0,-3])
C = np.array([0,np.sqrt(11)*0.5])
D = np.array([0,-np.sqrt(11)*0.5])

#Plotting the standard hyperbola
plt.plot(xStandardLeft[0,:],xStandardLeft[1,:],label='Hyperbola',color='b')
plt.plot(xStandardRight[0,:],xStandardRight[1,:],color='b')

# Plotting the foci and vertices
plt.plot(A[0],A[1],'o',color='g')
plt.text(0.5 ,3.5,'C1')
plt.plot(B[0],B[1],'o',color='g')
plt.text(0.5 ,-3.5,'C2')
plt.plot(C[0],C[1],'o',color='r')
plt.text(0.5 ,1.8,'V1')
plt.plot(D[0],D[1],'o',color='r')
plt.text(0.5 ,-1.8,'V2')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()