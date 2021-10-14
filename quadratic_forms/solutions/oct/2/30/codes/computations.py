import numpy as np
F = np.array([[0],[3]])
B = np.array([0, np.sqrt(11)/2])
n = np.array([[0],[1]])
c = 11/12
e = 6/np.sqrt(11)
I = np.identity(2)

V = (np.linalg.norm(n)**2)*I - (e**2)*n@n.T
u = c*(e**2)*n - (np.linalg.norm(n)**2)*F
f = (np.linalg.norm(n)**2)*(np.linalg.norm(F)**2) - (c**2)*(e**2)
print('V = ', V)
print('u = ', u)
print('f = ',f)