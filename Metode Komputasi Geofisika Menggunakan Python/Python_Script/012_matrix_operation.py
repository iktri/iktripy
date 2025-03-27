# import numpy as np

# X = np.genfromtxt('012_matrix1.txt')
# Y = np.genfromtxt('012_matrix2.txt')
# Z = np.genfromtxt('012_matrix3.txt')

# print(X)
# print(Y)
# print(Z)

# print(np.mat(X) + np.mat(Y))
# print(np.mat(X) - np.mat(Y))
# print(np.multiply(np.mat(X),np.mat(Y)))
# print(np.mat(X) / np.mat(Y))

#Contoh lain

# A = [[1, 3, 5], [2, 4, 8], [3, 7, 9]]
# B = [[1, 2, 1], [4, 1, 3], [6, 5, 2]]
#
# # scalar product
# # matrix operation (addition)
# for row in range(0, len(A)):
#     for col in range(0, len(A)):
#         print(A[row][col] + B[row][col], end=' ')
#     print()
#
# # matrix operation (subtraction)
# for row in range(0, len(A)):
#     for col in range(0, len(A[0])):
#         print(A[row][col] - B[row][col], end=' ')
#     print()
#
# # matrix operation (multiplication)
# print(len(A))
# for row in range(0, len(A)):
#     for col in range(0, len(A)):
#         print(A[row][col] * B[row][col], end=' ')
#     print()
#
# # matrix operation (division)
# for row in range(0, len(A)):
#     for col in range(0, len(A[0])):
#         print(A[row][col] / B[row][col], end=' ')
#     print()
#
# # matrix operation (power)
# for row in range(0, len(A)):
#     for col in range(0, len(A[0])):
#         print(A[row][col] ** B[row][col], end=' ')
#     print()
# #
# # matrix operation (modulus)
# for row in range(0, len(A)):
#     for col in range(0, len(A)):
#         print(A[row][col] % B[row][col], end=' ')
#     print()
#
# # matrix operation (floor division)
# for row in range(0, len(A)):
#     for col in range(0, len(A[0])):
#         print(A[row][col] // B[row][col], end=' ')
#     print()

#Operasi Perkalian matrix
# import numpy as np
#
# X = np.genfromtxt('012_matrix1.txt')
# Y = np.genfromtxt('012_matrix2.txt')
#
# print(X)
# print(Y)
# print(np.mat(X) * np.mat(Y))

# import numpy as np

# X = np.genfromtxt('012_matrix1.txt')
# print(X)
# print(np.mat(np.transpose(X)))

# import numpy as np
# A = [[1,2],[3,4]]
#
# print(A)
# At = np.transpose(A)
#
# for row in At:
#     for elem in row:
#         print(elem, end= ' ')
#     print()

# import numpy as np
# X = np.genfromtxt('012_matrix1.txt')
#
# print(X)
#
# from numpy.linalg import inv
# print(inv(np.mat(X)))
