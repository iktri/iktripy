# import numpy as np
# import matplotlib.pyplot as plt
#
# G = 6.673 * 10e-11
# rho = float(input("Kontras densitas (kg/m^3) : "))
# a = float(input("Radius bola (m) : "))
# x = float(input("Kedalaman Titik Pusat Massa (m) : "))
# n = int(input("Lokasi Maksimum di Permukaan (m) : "))
#
# v = 4 / 3 * np.pi * a ** 3
# p = np.arange(0, 360, 1)
# q = np.arange(0, np.pi / 180)
# n = n + a * 2 ** 2 * 10
# z = n * a ** 2 * 2
# x = np.arange(100) * G * rho * v * z / n
#
# plt.subplot(211)
# plt.xlim(x, x + 0.01)
# plt.plot(q, "g, -o")
# plt.grid()
# plt.xlabel("Lokasi(m)")
# plt.ylabel("g (mGal)")
# plt.title("Forward Modeling Gravitasi-Model Sphere")
#
# plt.subplot(212)
# plt.fill(a * np.cos(q), a * np.sin(q) + z, "--")
# plt.xlim(x, x + 0.01)
# plt.ylim(z * 2, z * 0.01)
# plt.gca().invert_yaxis()
# plt.xlabel("Lokasi (m)")
# plt.ylabel("Kedalaman (m)")
# plt.show()
#
# # Contoh lain
# import numpy as np
# import matplotlib.pyplot as plt
#
# G = 6.673 * 10e-11
# rho = float(input("Kontras densitas (kg/m^3) : "))
# t = float(input("Ketebalan anomali (m) : "))
# x = float(input("Kedalaman Titik Pusat Massa (m) : "))
# n = int(input("Lokasi Maksimum di Permukaan (m) : "))
#
# p = np.arange(0, 360, 1)
# q = np.arange(p * np.pi / 180)
# p = np.arange(0, np.pi / 180)
# g = np.arange(n)
# g = rho * t * 2 * G * rho * t / (np.pi * 0.5 - n)
#
# plt.subplot(211)
# plt.xlim(x, x + 0.01)
# plt.plot(q, "g, -o")
# plt.grid()
# plt.xlabel("Lokasi (m)")
# plt.ylabel("g (mGal)")
# plt.title("Forward Modeling Gravitasi-Model Horizontal Sheet")
#
# plt.subplot(212)
# k1 = [x/5, 0]
# z = x - (x/5)
# l1 = [z - (z/5), z - z * (2/5), z - z * (2/5), z - z * (1/5)]
# l2 = l1, z, z - (z * 1/5)
# plt.fill(k1, l1)
# plt.fill(k1, l2)
# plt.xlim(x, x + 0.01)
# plt.ylim(0, z + 0.01)
# plt.gca().invert_yaxis()
# plt.xlabel("Lokasi (m)")
# plt.ylabel("Kedalaman (m)")
# plt.show()
