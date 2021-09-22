## Author: Ganji Varshitha (AI20BTECH11009) ##
## Code to find the shortest distance between 2 skew lines and plotting the lines in 3D space ##
#importing required libraries

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
## Line 1 = (1,2,3) + lambda1(1,-3,2)
## Line 2 = (4,5,6) + lambda2(2,3,1)

#Generate line points
def line_gen(A,B):
  len =20
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(-2,2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B)
    x_AB[:,i]= temp1.T
  return x_AB

def point_gen(A,B,L):
  return A + L*B

def norm(a1,a2):
  x= np.sqrt(np.sum(np.square(a2-a1)))
  return x




#setting up plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_ylim([-4, 7])
ax.set_xlim([-1, 7])
ax.set_zlim([2, 7])


#Points for line 1
A1 = np.array([1,2,3]).reshape((3,1))
B1 = np.array([1,-3,2]).reshape((3,1))

#Generating line 1
x_AB = line_gen(A1,B1)
#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],color='g',label='Line 1')
 


#Plotting and labelling point A1

ax.scatter(1,2,3,'o',label='a1')
ax.text(1 * (1 + 0.1), 2 * (1 - 0.1) ,3*(1-0.1), "(1,2,3)")


#Points for line 1
A2 = np.array([4,5,6]).reshape((3,1))
B2 = np.array([2,3,1]).reshape((3,1))

#Generating line 1
x_AB = line_gen(A2,B2)
#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],color='r',label='Line 2')
 


#Plotting and labelling point A2

ax.scatter(4,5,6,'o',label='a2')
ax.text(4 * (1 + 0.1), 5* (1 - 0.1) ,6*(1-0.1), "(4,5,6)")


##Finding shortest distance between skew lines
B_array=np.concatenate((B2,B1),axis=1)
A=B_array.T@B_array

B=B_array.T@(A1-A2)
#Solving for lamba values using the equation Ax=B
lambda_v = np.linalg.solve(A,B)
# lamba_1 and -lambda_2 are the entries of above matrix
print('(lambda1,-lambda2)(calculated)=',lambda_v)

#Verifying with built in least square function
Y= np.linalg.lstsq(A,B)
print('(lambda1,-lambda2)(inbuilt)=',Y[0])

#positional vectors of end points of shortest distance line 
p1=point_gen(A1,B1,lambda_v[0,0])
p2=point_gen(A2,B2,-lambda_v[1,0])

#Finding shortest distance
d=norm(p1,p2)

print('The shortest distance between skew lines is: ',d)


#plotting shortest line
p=np.concatenate((p1,p2),axis=1)



plt.plot(p[0,:],p[1,:],p[2,:],color='b',label='shortest line')

#Plotting and labelling point p1,p2

ax.scatter(-0.4736 , 6.4210 , 0.0526 ,'c',label='p1')
ax.text(-0.4736 * (1 + 0.1), 6.4210* (1 - 0.1) ,0.0526*(1-0.1),"p1")

ax.scatter(5.05263, 6.57894, 6.5263,'y',label='p2')
ax.text(5.05263 * (1 + 0.1), 6.57894* (1 - 0.1) ,6.5263*(1-0.1),"p2")





plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.legend(loc='best')


plt.show()



