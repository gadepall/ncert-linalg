import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
m=np.reshape([1,1],(2,1))
#print(m)
V=np.reshape([1,0,0,0],(2,2))
#print(V)
u=np.reshape([0,-2],(2,1))
f=0
q=np.reshape([-2,0],(2,1))
mu1=(-m.T@(V@q+u)+np.sqrt((m.T@(V@q+u))**2-(q.T@V@q+2*u.T@q+f)*(m.T@V@m)))/(m.T)@V@m
mu2=(-m.T@(V@q+u)-np.sqrt((m.T@(V@q+u))**2-(q.T@V@q+2*u.T@q+f)*(m.T@V@m)))/(m.T)@V@m
print(mu1,mu2)     #path to my scripts

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 5
y = np.linspace(-4,4,len)

#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 

#def line_dir_pt
def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

#
##Generating the secant
k1 = 2
k2 = -2



x=np.linspace(-6,6)
x1=np.linspace(-6,6)
y1=(x1+2)
#Generating the Standard parabola
y =(x*x)/4
xStandardparab = np.vstack((x,y))

#coordinates of each point
l = np.array([2-2*np.sqrt(3),4-2*np.sqrt(3)])
k = np.array([2+2*np.sqrt(3),4+2*np.sqrt(3)])
m=np.array([2+2*np.sqrt(3),0])
n=np.array([2-2*np.sqrt(3),0])
c=np.array([0,0])

#plotting points
plt.plot(m[0], m[1], 'o',color='b')
plt.text(m[0] + 0.3, m[1] + 0.3, 'M')
plt.plot(n[0], n[1], 'o',color='orange')
plt.text(n[0] - 0.3, n[1] -0.8, 'N')
plt.plot(l[0], l[1], 'o')
plt.text(l[0] - 0.3, l[1] + 0.3, 'L')
plt.plot(k[0], k[1], 'o')
plt.text(k[0] - 1.3, k[1] + 0.3, 'K')
plt.plot(c[0], c[1], 'o')
plt.text(c[0] - 0.3, c[1] + 0.3, 'C')

#Plotting all lines
plt.axhline(y=0,color='gray')
plt.plot(x1, y1, '-', label='$y = x+2$',color='g')
plt.axvline(x=2+2*np.sqrt(3),color='blue',label = 'x=$2+2\sqrt{3}$' ,linestyle='--')
plt.axvline(x=2-2*np.sqrt(3),color='orange',label ='x=$2-2\sqrt{3}$',linestyle='--')

#Plotting the actual parabola
plt.plot(xStandardparab[0,:],xStandardparab[1,:],label='x^2 = 4y',color='r')

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()