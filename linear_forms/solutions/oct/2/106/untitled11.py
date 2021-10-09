from sympy import *
import numpy as np
import matplotlib.pyplot as plt

x, y, k = symbols('x y k')

Q= np.array([x,y])
c = k**2-7*k+6
n = np.array([k-3,-(4-k**2)])
# Eq = np.dot(n,Q) + c
Eq = n@Q
print(Eq)

def line_gen(A,B):
  len = 10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

labels = ['(0 5)X = 6','(-5 0)X = -24','(1 0)X = -4','(-2 -3)X = 0','(3 32)X = 0']
l = 0
####  a) Line Parallel to x-axix  ######
#################################################
##n=(0  1)if the line is parallel to x-axis
q = np.array([1,0])@n   ###Equation of x-axis is(1  0)x=0
sol= list(solveset(q, k)                                  )
print(sol)
for i in sol:
  Eqq = Eq.subs(k,i)
  print(Eqq)
  P1,P2 = np.array([33]+list(solveset(Eqq,y))),np.array([-33]+list(solveset(Eqq,y)))
  x_FP = line_gen(P1,P2)
  plt.plot(x_FP[0,:],x_FP[1,:],label= labels[l])
  l = l + 1
  plt.plot(P1[0], P1[1], 'o')
  plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1), 'A')
  plt.plot(P2[0], P2[1], 'o')
  plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.1), 'B')

####  b) lines parallel to y- axis  ######
#################################################
##n=(1  0)if the line is parallel to y-axis
q = np.array([0,1])@n   ###Equation of y-axis is(0  1)x=0
sol= list(solveset(q, k))
print(sol)
for i in sol:
  Eqq = Eq.subs(k,i)
  print(Eqq)
  P1,P2 = np.array(list(solveset(Eqq,x))+[33]),np.array(list(solveset(Eqq,x))+[-33])
  x_FP = line_gen(P1,P2)
  plt.plot(x_FP[0,:],x_FP[1,:],label= labels[l])
  l = l + 1
  plt.plot(P1[0], P1[1], 'o')
  plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1), 'A')
  plt.plot(P2[0], P2[1], 'o')
  plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.1), 'B')

####  c) Lines passing through Origin  ######
#################################################
##c=0   if the line passes through origin
sol = list(solveset(c, k))    ###solving for k^2-7k+6
print(sol)
for i in sol:
  Eqq = Eq.subs(k,i)
  print(Eqq)
  Eqqx1= Eqq.subs(x,33)
  Eqqx2= Eqq.subs(x,-33)
  P1,P2 = np.array([33]+list(solveset(Eqqx1,y))),np.array([-33]+list(solveset(Eqqx2,y)))
  x_FP = line_gen(P1,P2)
  plt.plot(x_FP[0,:],x_FP[1,:],label= labels[l])
  l = l + 1
  plt.plot(P1[0], P1[1], 'o')
  plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1), 'A')
  plt.plot(P2[0], P2[1], 'o')
  plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.1), 'B')
  
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower left')
plt.axis('equal')
plt.show()
