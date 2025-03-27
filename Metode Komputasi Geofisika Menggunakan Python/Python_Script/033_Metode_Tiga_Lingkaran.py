# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.sparse.linalg import lsqr
#
# Data = np.genfromtxt("033_datagempa.dat")
# STA = ['KRL', 'BUS', 'MRT']
# tp = Data[:, 1]
# ts = Data[:, 2]
# x = Data[:, 3]
# y = Data[:, 4]
#
# K = 8
# n = len(tp)
# t = (ts - tp) * K
# ln = len(tp)
# teta = np.linspace(0, 2 * np.pi, 100)
# X = []
# Y = []
# b = []
# c = []
#
# for i in range(0, n):
#     X = (r[i] * np.cos(teta)) + x[i]
#     Y = (r[i] * np.sin(teta)) + y[i]
#     # create the figure
#     plt.plot(X, Y, label=i + 1)
#     plt.xlabel('Metode Tiga Lingkaran', color='k')
#     plt.xlabel('X (km)', color='k')
#     plt.ylabel('Y (km)', color='k')
#     plt.tick_params(axis="both", labelcolor="#610203")
#     plt.grid()
#     plt.axis('equal')
#
#     if i != n - 1:
#         c.append((x[i] ** 2 + y[i] ** 2) - (x[i + 1] ** 2 + y[i + 1] ** 2))
#         c.append(((t[i] ** 2 - t[i + 1] ** 2) - 2 * (x[i] * x[i + 1] + y[i] * y[i + 1])))
#
#     elif i == n - 1:
#         c.append(((x[0] ** 2 + y[0] ** 2) - (x[i] ** 2 + y[i] ** 2)))
#         c.append((t[0] ** 2 - t[i] ** 2) - 2 * (x[0] * x[i] + y[0] * y[i]))
#
# b = np.array(b)
# c = np.array(c)
#
# # jarak epicenter
# A = lsqr(c, b)
# A1 = A[0][0]
# A2 = A[0][1]
# print('Lokasi Episenter adalah (', '%.2f' % A1, ',', '%.2f' % A2, ')')
# plt.plot(A1, A2, 'o', label='epicenter')
#
# for j, stat in enumerate(STA):
#     x1 = x[j]
#     y1 = y[j]
#     plt.scatter(x1, y1, marker='^', color='blue')
#     plt.text(x1 + 0.3, y1 + 0.3, stat, fontsize=9)
#
# plt.legend()
# plt.show()