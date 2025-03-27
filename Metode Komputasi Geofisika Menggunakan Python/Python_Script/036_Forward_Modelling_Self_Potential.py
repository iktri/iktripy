# import numpy as np
# import matplotlib.pyplot as plt
#
# k = int(input("Nilai K = "))
# h = int(input("Kedalaman Titik Tengah Anomali (h) = "))
# x0 = int(input("Titik awal pengukuran (x0) = "))
# y = int(input("Jarak pengukuran (y) = "))
# a = int(input("Setengah panjang lempeng (a) = "))
# theta = int(input("Sudut inklinasi (theta) = "))
#
# theta = (np.pi / 180) * theta
#
# x = np.arange(0, y)
#
# c = []
# for i in range(0, len(x)):
#     b = (((x[i] - x0) + a * np.cos(theta)) ** 2 + (h - a * np.sin(theta)) ** 2)
#     c.append(((x[i] - x0) - a * np.cos(theta)) ** 2 + (h + a * np.sin(theta)) ** 2)
#     v = np.append(np.log(b / c))
#
# v = np.array(v)
#
# plt.subplot(311)
# plt.plot(x, v, 'r')
# plt.xlim(min(x), max(x))
# plt.grid()
# plt.gca().invert_yaxis()
# plt.xlabel("Posisi (m)")
# plt.ylabel("V (m/s)")
# plt.title("Modeling SP - Model Lempeng")
#
# plt.subplot(313)
# x1 = [x0 + a * np.cos(theta), x0 - a * np.cos(theta), x0]
# y1 = [h, h + 50, h - 50]
#
# plt.fill(x1, y1, facecolor='b', alpha=0.5)
# plt.xlim(min(x), max(x))
# plt.xticks(np.arange(min(x), max(x), 0.01))
# plt.ylim(0, 2.5 * h)
# plt.grid()
# plt.gca().invert_yaxis()
# plt.xlabel("Posisi (m)")
# plt.ylabel("Kedalaman (m)")
# plt.show()
#
# # Contoh lain
# import numpy as np
# import matplotlib.pyplot as plt
#
# k = int(input("Nilai K = "))
# z = int(input("Kedalaman Anomali (z) = "))
# d = int(input("Titik awal pengukuran (d) = "))
# y = int(input("Jarak pengukuran (y) = "))
# theta = int(input("Sudut Polarisasi (theta) = "))
#
# theta = (np.pi / 180) * theta
#
# def fungsi_model_bola():
#     t = int(input("Jari-jari Model Bola = "))
#     x = np.arange(360)
#     s = []
#
#     for i in range(0, len(x)):
#         s.append(((x[i] - d) * np.cos(theta)) / ((((x[i] - d) ** 2) + (z ** 2)) ** 1.5))
#
#     v = k * np.array(s)
#     unit = k * np.sin(theta) + z
#
#     plt.subplot(211)
#     plt.plot(x, v, 'r')
#     plt.xlim(min(x), max(x))
#     plt.grid()
#     plt.xlabel("Posisi (m)")
#     plt.ylabel("Delta g (mGal)")
#     plt.title("Modeling SP - Model Bola")
#
#     plt.subplot(212)
#     plt.fill(unit, z, facecolor='b', alpha=0.5)
#     plt.xlim(min(x), max(x))
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.grid()
#     plt.gca().invert_yaxis()
#     plt.xlabel("Posisi (m)")
#     plt.ylabel("Kedalaman (m)")
#
#     plt.show()
#     return
#
# fungsi_model_bola()
#
#
# def fungsi_model_silinder():
#     t = int(input("Jari-jari Model Silinder = "))
#     x = np.arange(0, 360)
#     s = []
#
#     for i in range(0, len(x)):
#         a1 = ((x[i] - d) * np.cos(t)) + (z * np.sin(t))
#         b1 = (((x[i] - d) ** 2) + (z ** 2)) ** 2
#         s.append(a1 / b1)
#
#     v = k * np.array(s)
#     xunit = t * np.cos(th) + d
#     yunit = t * np.sin(th) + z
#
#     plt.subplot(211)
#     plt.plot(x, v, 'r')
#     plt.xlim(min(x), max(x))
#     plt.grid()
#     plt.xlabel("Posisi (m)")
#     plt.ylabel("Delta g (mGal)")
#     plt.title("Modeling SP - Model Silinder")
#
#     plt.subplot(212)
#     plt.fill(xunit, yunit, 'r')
#     plt.xlim(min(x), max(x))
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.grid()
#     plt.gca().invert_yaxis()
#     plt.xlabel("Posisi (m)")
#     plt.ylabel("Kedalaman (m)")
#
#     plt.show()
#     return
#
#
# i1 = 0
# while i1 < 1000000:
#     print("Masukkan angka 1 untuk Model Bola dan angka 2 untuk Model Silinder")
#     Variabel = int(input("Masukkan Model Yang Ingin Dituju(1/2): "))
#
#     if Variabel == 1:
#         print(fungsi_model_bola())
#     elif Variabel == 2:
#         print(fungsi_model_silinder())
#     else:
#         print("Kode Yang Anda Input Error")
#
#     lanjut = input("Perhitungan yang Lain untuk parameter yang sama? (y/n) : ")
#     if lanjut == "y":
#         i1 += 1
#     else:
#         print("Terima Kasih")
#         break
#
