#Assignment 4
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#Defining the points
P = np.array([0, 2])
Q = np.array([0, -2])
A = np.array([1, 2 - sqrt(3)])
B = np.array([1, -2 - sqrt(3)])

#Plotting the points
plt.plot(P[0], P[1], 'o')
plt.plot(Q[0], Q[1], 'o')
plt.plot(A[0], A[1], 'o')
plt.plot(B[0], B[1], 'o')
plt.text(P[0], P[1] * (1 - 0.2), 'P')
plt.text(Q[0], Q[1] * (1 - 0.1), 'Q')
plt.text(A[0], A[1] * (1 - 1.6), 'A')
plt.text(B[0], B[1] * (1 - 0.1), 'B')

#Drawing the line
plt.plot(np.array([A[0], P[0]]),np.array([A[1], P[1]]), 'b', label="$AP$")
plt.plot(np.array([B[0], Q[0]]),np.array([B[1], Q[1]]), 'r', label="$BQ$")
plt.grid()
plt.legend()
plt.show()
