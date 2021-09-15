from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


A1 = np.array([1,2,3]).reshape((3,1))
A2 = np.array([3,1,6]).reshape((3,1))
B1 = np.array([-29,3.4624,23]).reshape((3,1))
B2 = np.array([5.19636,11,-44]).reshape((3,1))
C1 = np.array([31,0.53576,-17]).reshape((3,1))
C2 = np.array([0.80364,-9,56]).reshape((3,1))
#Generating all lines
x_C1B1 = line_gen(C1,B1)
x_C2B2 = line_gen(C2,B2)
#plotting line
plt.plot(x_C1B1[0,:],x_C1B1[1,:],x_C1B1[2,:],color='g',label='L1')
plt.plot(x_C2B2[0,:],x_C2B2[1,:],x_C2B2[2,:],color='b',label='L2')
plt.legend()
ax.view_init(-150,60)
ax.scatter(3.196094,1.892816,1.535936,'o',color='r')
ax.text(3.196094 + 5 , 1.892816 + 5 ,1.535936+5, "$P(\dfrac{4+5k}{1+5k}, \dfrac{2+8k}{1+5k}, \dfrac{1+15k}{1+5k})$")
plt.title('$k=\dfrac{-13+\sqrt{205}}{18}$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()



fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
A1 = np.array([1,2,3]).reshape((3,1))
A2 = np.array([3,1,6]).reshape((3,1))
B1 = np.array([-29,-28.35313,23]).reshape((3,1))
B2 = np.array([-42.5297,11,-44]).reshape((3,1))
C1 = np.array([31,32.35313,-17]).reshape((3,1))
C2 = np.array([48.5297,-9,56]).reshape((3,1))
#Generating all lines
x_C1B1 = line_gen(C1,B1)
x_C2B2 = line_gen(C2,B2)
#plotting line
plt.plot(x_C1B1[0,:],x_C1B1[1,:],x_C1B1[2,:],color='g',label='L1')
plt.plot(x_C2B2[0,:],x_C2B2[1,:],x_C2B2[2,:],color='b',label='L2')
plt.legend()
ax.scatter(0.544646, 1.539286, 3.303569,'o',color='r')
ax.text(0.544646+5, 1.539286+5, 3.303569+5, "$P(\dfrac{4+5k}{1+5k}, \dfrac{2+8k}{1+5k}, \dfrac{1+15k}{1+5k})$")
plt.title('$k=\dfrac{-13-\sqrt{205}}{18}$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()