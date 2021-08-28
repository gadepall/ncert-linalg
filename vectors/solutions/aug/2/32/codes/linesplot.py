from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# Plotting the lines
A = np.array([1,2,3]).reshape((3,1))
B = np.array([4,5,7]).reshape((3,1))
C = np.array([-4,3,-6]).reshape((3,1))
D = np.array([2,9,2]).reshape((3,1))

AB = B - A
CD = D - C
print('Direction vector for line AB is :\n',AB)
print('Direction vector for line CD is :\n',CD)

L_AB = np.empty((2,3),float)
L_AB[0,:] = A[:,0]
L_AB[1,:] = B[:,0]

L_CD = np.empty((2,3),float)
L_CD[0,:] = C[:,0]
L_CD[1,:] = D[:,0]

plt.plot(L_AB[:,0],L_AB[:,1],L_AB[:,2],'r',label="AB")
plt.plot(L_CD[:,0],L_CD[:,1],L_CD[:,2],'g',label="CD")

ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.scatter(D[0],D[1],D[2],'o')
ax.text(1,2,3, "A", color='red')
ax.text(4,5,7, "B", color='red')
ax.text(-4,3,-6, "C", color='red')
ax.text(2,9,2, "D", color='red')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()

# Angle between the lines
dot = AB.T @ CD 
angle = math.acos(dot / (np.linalg.norm(AB)*np.linalg.norm(CD)))

print("The angle between the lines  :",angle*180/math.pi,"degrees")