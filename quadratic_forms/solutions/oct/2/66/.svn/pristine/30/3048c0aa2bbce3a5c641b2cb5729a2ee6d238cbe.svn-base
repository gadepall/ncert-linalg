import numpy as np
import matplotlib.pyplot as plt

def parabola(y):
    return y**2/4

def line_(y):
    return y-1

y=np.linspace(-3,3,60)

plt.plot(line_(y[30:]),y[30:],'g',label="$y-x=1$")
plt.plot(parabola(y),y,'r',label="$y^2=4x$")
plt.scatter(1,2,label="point of tangency")
plt.text(1+0.1,2-.1,"$(1,2)$")
plt.grid()
plt.legend()
plt.show()

