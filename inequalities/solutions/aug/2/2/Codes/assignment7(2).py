import numpy as np
import matplotlib.pyplot as plt
 
#Intersection of two lines
def line_intersect(n1,c1,n2,c2):
  N=np.vstack((n1,n2))
  p = np.array([c1,c2])
   #Intersection
  P=np.linalg.inv(N)@p
  return P
 
#Line Parameters
n1 = np.array([5,4])
n2 = np.array([1,0])
n3 = np.array([0,1])
c1 = 40
c2 = 2
c3 = 3
 
#Intersection of the lines
A=line_intersect(n1,c1,n2,c2)
B=line_intersect(n2,c2,n3,c3)
C=line_intersect(n3,c3,n1,c1)
points = np.array((A,B,C))
 
#Filling up the desired region
plt.fill(points[:,0], points[:,1], 'p', alpha=0.5)
 
#Plotting points of Intersection
plt.plot(A[0], A[1], 'o')
plt.text(A[0]+0.05, A[1] * (1 ) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1+0.04 ), B[1] * (1)-0.2 , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.01), C[1] * (1 + 0.02) , 'C')
 
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid() # minor
 
plt.show()
