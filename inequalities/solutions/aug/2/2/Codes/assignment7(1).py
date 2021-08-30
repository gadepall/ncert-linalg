import numpy as np
import matplotlib.pyplot as plt
 
#Generate line points
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
 
#Generating and plotting line 5x+4y = 40
A=np.array([0,10])
B=np.array([8,0])
AB=line_gen(A,B)
plt.plot(AB[0,:],AB[1,:],label='5x+4y=40')
 
#Generating and plotting line x=2
C=np.array([2,0])
D=np.array([2,10])
CD=line_gen(C,D)
plt.plot(CD[0,:],CD[1,:],label='x=2')
 
#Generating and plotting line y=3
E=np.array([0,3])
F=np.array([8,3])
EF=line_gen(E,F)
plt.plot(EF[0,:],EF[1,:],label='y=3')
 
#Shading Required Region
x1=[2,5.6,2]
y1=[7.5,3,3]
plt.fill(x1,y1)
 
#Labelling points
plt.plot(2,3,'o',color='r')
plt.text(2,3,'A(2,3)')
plt.plot(28/5,3,'o',color='r')
plt.text(28/5,3,'B(28/5,3)')
plt.plot(2,15/2, 'o', color='r')
plt.text(2,15/2,'C(2,15/2)')
 
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
