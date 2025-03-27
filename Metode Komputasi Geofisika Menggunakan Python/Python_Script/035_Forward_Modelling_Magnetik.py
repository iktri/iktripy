# import numpy as np
# import matplotlib.pyplot as plt
#
# Uo = 1.256 * (10 ** 3)
# Mz = 1
# z1 = int(input("Kedalaman batas atas objek (m): "))
# z2 = int(input("Kedalaman batas bawah objek (m): "))
# w = int(input("Lebar lapisan (m): "))
# xo = int(input("Lokasi objek (m): "))
# n = int(input("Lokasi pengukuran maksimum (m): "))
#
# x = np.arange(-w, w)
# f = []
#
# for i in range(len(x)):
#     a1 = np.arctan((x[i] - xo + w) / z1)
#     a2 = np.arctan((x[i] - xo - w) / z1)
#     a3 = np.arctan((x[i] - xo + w) / z2)
#     a4 = np.arctan((x[i] - xo - w) / z2)
#     Bz = (Uo * Mz * (a1 - a2 - a3 + a4)) / (2 * np.pi)
#     f.append(Bz)
#
# plt.subplot(211)
# plt.plot(x, f, 'o', markersize=4)
# plt.grid()
# plt.xlabel("Posisi (m)")
# plt.ylabel("Anomali Magnetik (nT)")
# plt.title("Modeling Magnetik Crustal Block")
#
# plt.subplot(212)
# X = [xo - w, xo + w, xo + w, xo - w]
# Z = [z1, z1, z2, z2]
# plt.plot(X, Z, 'o')
# plt.fill(X, Z)
# plt.xlim(-w, w)
# plt.ylim(0, z2 + 30)
# plt.gca().invert_yaxis()
# plt.xlabel("Posisi (m)")
# plt.ylabel("Kedalaman (m)")
# plt.show()
#
# # Contoh lain
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Parameter
# K = 50000  # Konstanta susceptibilitas
# I0 = 50  # Intensitas medan magnet bumi
# D = 10  # Sudut inklinasi medan magnet bumi
# h = 40  # Kedalaman
# t = 20  # Ketebalan
# a = 120  # Panjang
# x0 = 0  # Lokasi pusat
# n = 100  # Jumlah titik pengukuran
#
# x = np.arange(-a, a, 1)  # Posisi pengukuran
# I = np.cos(K * (np.pi / 180)) / H
#
# I1 = np.degrees(np.arctan(np.tan(np.radians(I0)) / np.sin(np.radians(a))))
# D0 = np.radians(I1)
# D1 = np.radians(I0)
# P = 2 * K * t * (1 - (np.cos(D0) * np.radians(I0)) ** 2) - (np.cos(D1) * np.radians(I0)) ** 0.5
#
# M = 0
# H = []
#
# for i in range(len(x)):
#     Hx = P * ((x[i] - x0) * np.sin(D0) + (h * np.cos(D0))) / ((x[i] - x0) ** 2 + h ** 2)
#     H.append(Hx)
#
# plt.subplot(211)
# plt.plot(x, H, 'o', markersize=2)
# plt.grid()
# plt.xlabel("Posisi (m)")
# plt.ylabel("Anomali Magnetik (nT)")
# plt.title("Modeling Magnetik Thin Sheet")
#
# plt.subplot(212)
# x_it = t / 2 * (50 / np.tan(a * np.pi / 180)) + t / 2, (50 / -np.tan(a * np.pi / 180)) - t / 2, t / 2, -t / 2
# y_it = [H, H, x0, 80]
# plt.fill(x_it, y_it)
# plt.xlim(-a, a + 70)
# plt.gca().invert_yaxis()
# plt.xlabel("Posisi (m)")
# plt.ylabel("Kedalaman (m)")
# plt.show()
