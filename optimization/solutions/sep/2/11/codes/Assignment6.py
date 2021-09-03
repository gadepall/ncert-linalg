#from coeffs import *
from cvxpy import *
import numpy as np
import matplotlib.pyplot as plt

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

  #Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2]) 
  #Intersection
  P=np.linalg.inv(N)@p
#  P=np.linalg.inv(N.T)@p
  return P

A = np.array(( [1, -1], [-1, 1 ])).T
b = np.array([ -1,0 ]).reshape((2,-1))
c = np.array([ 1, 1 ])  #Z


x = Variable((2,1),nonneg=True)
#Maximum function
f = c@x
lp_obj_mx = Maximize(f)
#Constraints
constraints = [A.T@x <= b]

#solution
Problem(lp_obj_mx, constraints).solve()
print("Maximum= ",f.value)


# Construct lines
x = np.array([0,200])
y1 = []
y2 = []

for i in range(2):
  y1.append(1+x[i]) 
  
  y2.append(1*x[i])     
  

# plot
plt.plot(x, y1, label=r'$y\leq(1+x)$')
plt.plot(x, y2, label=r'$y\geq(x)$')
y3=np.zeros(x.shape)
plt.plot(x,y3,label="Y=0")
plt.plot(y3,x,label="X=0")


plt.xlim((-20, 100))
plt.ylim((-20, 250))
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()

#if using termux
plt.savefig('./figs/Assignment6.pdf')
plt.savefig('Figure.png')
subprocess.run(shlex.split("termux-open ./figs/Assignment6.pdf"))
#else
#plt.show()
