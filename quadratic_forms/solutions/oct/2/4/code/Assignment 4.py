import numpy as np
import math
import matplotlib.pyplot as plt
r = 2 
c=np.array([1,0])                           
angle = np.linspace(0, 2*np.pi, 1000) 
x1 = np.cos(angle)*r+1
y1 = np.sin(angle)*r
plt.plot(x1,y1,label="circle")
#plt.figure(figsize=(3, 3)
plt.grid()
plt.axis('equal')
O=np.linalg.norm(c)
f=(O**O)-(r**r)
u= np.array([-1,0])
U= u .T @ u
n=np.array([0,1])
N=n.T @ n
k1=+math.sqrt(U-f/N)
print(k1)
k2=-math.sqrt(U-f/N)
print(k2)
n1=[0,k1]
tangent1=n1-u
print(tangent1)
n2=[0,k2]
tangent2=n2-u
print(tangent2)
plt.scatter(1,0,marker="x",color="black")
plt.text(1,0, "O", color='blue')
plt.axhline(y =2,color="green",label="Tangent1")
plt.scatter(1,2,marker="x")
plt.text(1,2, "P(1,2)", color="red")
plt.axhline(y =-2,color="yellow",label="Tangent2")
plt.scatter(1,-2,marker="x")
plt.text(1,-2, "P2(1,-2)", color="red")
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0.)
plt.xlabel('$X$')
plt.ylabel('$Y$')