#Assignment 5
import numpy as np
import cmath
import matplotlib.pyplot as plt
from numpy import linalg

n = 1000
x = np.linspace(-10,10, n)
#Equation: 4x^2 + 3x + 5

V = np.array(([4, 0],[0, 0]))
u = np.array(([3/2,-3/2]))
f = 5

#Finding the eigenvalues and eigenvectors
D_vec,P = linalg.eig(V)
D = np.diag(D_vec)

#Computing the value of eta
eta = u @ P[:,1]
foc = -(2 * eta)/D_vec[0]

#Generating the points for the parabola
x_para = (x**2/foc)/4

p1 = P[:,1]
p2 = P[:,0]

cA = np.block([[u + eta*P[:,1]],[V]])
cb = np.block([[-f],[(eta*P[:,1]-u).reshape(-1,1)]])
c = linalg.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()

#To check if there are real roots
result = (p1.T @ c) * ((p2.T @ V) @ p2)
print(result)
if result > 0:
    print("The quadratic equation does not have real roots")
else:
    print("The quadratic equation has real roots")

m = np.array(([1,0]))
q = np.array(([0,0]))
#To find the roots
mu1 = ((-1 * (m.T @ ((V@q) + u))) / ((m.T@V)@m)) + (cmath.sqrt(pow((m.T @ ((V@q) + u)), 2) - (q.T@V@q + 2*u.T@q + f)*((m.T@V)@m))/((m.T@V)@m))
mu2 = ((-1 * (m.T @ ((V@q) + u))) / ((m.T@V)@m)) - (cmath.sqrt(pow((m.T @ ((V@q) + u)), 2) - (q.T@V@q + 2*u.T@q + f)*((m.T@V)@m))/((m.T@V)@m))
print("Roots of the equation: ")
print(mu1)
print(mu2)
xStandardparab = np.vstack((x,x_para))
xActualparab = P@xStandardparab + c[:,np.newaxis]

#Plotting the standard and actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='Standard Parabola',color='b')
plt.plot(xActualparab[0,:],xActualparab[1,:],label='$4x^2 + 3x + 5$',color='r')
plt.plot([i for i in range(-10,10)] , [0 for i in range(-10,10)] , 'k-',label = "x-axis" )

plt.legend(loc='best')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid()
plt.show()
