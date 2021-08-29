# -*- coding: utf-8 -*-
"""SIgnal_1ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pxP0sV808E0HPGVXTmLD0G66I8pKrRq8
"""

# Importing all the libraries
import numpy as np
import matplotlib.pyplot as plt
from sympy.matrices import Matrix

# Input all the given vectors
A=np.array([3,0])
B=np.array([-2,-2])
C=np.array([8,2])

# Printing the vectors
print("A: ",A)
print("B: ",B)
print("C: ",C)

# Making the M matrix
M=Matrix([B-A,C-A])

# Printing the M matrix
print("M =",M)

# Printing the rref of M matrix
M_rref = M.rref()
print("\nThe reff of matrix M is given as\n : ",M_rref)

# Calculating the rank of Matrix M 
N=np.array([B-A,C-A])
print ("\nrank of matrix = ",np.linalg.matrix_rank(N))

# Plotting the points
plt.plot(A[0], A[1], 'o')
plt.text(A[0], A[1] , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] , B[1] , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0], C[1]  , 'C')
plt.plot(np.array([3,-2]),np.array([0,-2]), 'b', label="$AB$")
plt.plot(np.array([-2,8]), np.array([-2,2]),'r', label="$BC$")
plt.plot(np.array([3,8]), np.array([0,2]),'g', label="$CA$")
plt.grid(True)
plt.legend(loc='lower right')
plt.show()
print("Hence the points are collinear")