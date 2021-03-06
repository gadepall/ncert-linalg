# -*- coding: utf-8 -*-
"""Assignment_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1siE73KB8RZkeJU3FgnP3kFuX_j7mx_bU
"""

#Import the required libraries
import numpy as np
from matplotlib import pyplot as plt

#Declaring the matrices
A = np.array([[-1, 2, 3], [5, 7, 9], [-1, 1, 1]])
B = np.array([[-4, 1, -5], [1, 2, 0], [1, 3, 1]])

#Printing (A-B)'
print("(A-B)'=",(A-B).T)

#Printing A'-B'
print("A'-B'=",A.T-B.T)
print("Hence we conclude that (A-B)' = A'-B'.")