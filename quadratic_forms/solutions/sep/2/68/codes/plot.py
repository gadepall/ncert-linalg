import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

fig = plt.figure()
len = 100
y = np.linspace(-4,4,len)

def parab_gen(y,a):
    x = y**2/a
    return x

def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

V = np.array(([1,0],[0,0]))
u = np.array(([0,1]))
f = -3

D_vec,P = LA.eig(V)
if D_vec[0] != 0:
    temp = D_vec[0]
    D_vec[0] = D_vec[1]
    D_vec[1] = temp
    P[:,[0,1]] = P[:,[1,0]]
D = np.diag(D_vec)
p = P[:,0]
eta = 2*u@p

foc = -eta/D_vec[1]

x = parab_gen(y,foc)

cA = np.vstack((u+eta*0.5*p,V))
cb = np.vstack((-f,(eta*0.5*p-u).reshape(-1,1)))
c = LA.lstsq(cA,cb,rcond=None)[0]
c = c.flatten()

xStandardparab = np.vstack((x,y))

xActualparab = P@xStandardparab + c[:,np.newaxis]

k1 = 3
k2 = -7
m = 1
q = np.array([1,1])
x_AB = line_dir_pt(m,q,k1,k2)
plt.plot(x_AB[0,:],x_AB[1,:],label='Normal',color='b')

plt.plot(xActualparab[0,:],xActualparab[1,:],label='Given Parabola',color='r')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()
