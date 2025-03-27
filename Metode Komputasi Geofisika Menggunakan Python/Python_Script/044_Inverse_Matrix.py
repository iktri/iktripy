# Singular-value decomposition
import numpy as np
from scipy.linalg import svd

# define a matrix
A = np.array([[1, -2], [1, -2]])

# SVD
U, S, VT = svd(A)

# S max diagonal
S_ = []
for i in range(len(A)):
    b = []
    for j in range(len(A[0])):
        c = 0
        b.append(c)
    S_.append(b)

for m in range(len(S)):
    for n in range(len(S[0])):
        if m == n:
            S_[m][n] = S[m]

SL = []
for i in range(len(S_)):
    b = []
    for j in range(len(S_[0])):
        c = 0
        b.append(c)
    SL.append(b)

for i in range(len(S_)):
    for j in range(len(S_[0])):
        if 0.000001 >= S_[i][j] >= 0:
            SL[i][j] = 0
        elif 0 - 0.000001 <= S_[i][j] <= 0:
            SL[i][j] = 0
        else:
            SL[i][j] = 1 / S_[i][j]

print("\nU:\n", U)
print("\nS:\n", np.array(S_))
print("\nV^T:\n", VT)
print("\n\nA:\n", np.transpose(VT))
print("\nA1:\n", np.transpose(VT)*np.mat(S_)*np.transpose(U))
print("\nAinv:\n", A1)
