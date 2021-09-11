## Author: Ganji Varshitha (AI20BTECH11009) ##
## Code to plot the region in first quadrant bounded by the circle x^Tx = 4 and lines x=0 and x=2 ##
#importing required libraries
import numpy as np 
import matplotlib.pyplot as plt 

#Generating line points
def line_gen(A,B):
  len =20
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(-2,2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

l = np.array([0,-1])
m = np.array([0,1])
O = np.array([0,0])
C = np.array([2,2])
A = np.array([0,2])
B = np.array([2,0])

x_points_1 = [2*np.cos(theta*np.pi/180) for theta in range(90)]
y_points_1 = [2*np.sin(theta*np.pi/180) for theta in range(90)] 

x_points_2 = [2*np.cos(theta*np.pi/180) for theta in range(90)]
y_points_2 = [0 for theta in range(90)]

x_points = x_points_1 + x_points_2
y_points = y_points_1 + y_points_2

x_lm = line_gen(l,m)
x_rs=line_gen(B,C)

len = 200
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = np.sqrt(4)*np.cos(theta)
x_circ[1,:] = np.sqrt(4)*np.sin(theta)
x_circ = (x_circ.T + O).T

#Filling the region in black
plt.fill_between([0,0,2],[0,2,0],color = 'black')
plt.fill_between(x_points,y_points,color = 'black')


#Plotting the circle and lines
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle: x^Tx = 4$')
plt.plot(O[0],O[1],'o')
plt.plot(A[0],A[1],'o')
plt.plot(B[0],B[1],'o')
plt.plot(x_lm[0,:],x_lm[1,:],label='$L_1: x = 0$')
plt.plot(x_rs[0,:],x_rs[1,:], label='$L_2: x = 2$')

plt.text(O[0],O[1]+ 0.1,'O')
plt.text(A[0],A[1]+0.1,'A')
plt.text(B[0]+0.05,B[1]+0.05,'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')

plt.show()
