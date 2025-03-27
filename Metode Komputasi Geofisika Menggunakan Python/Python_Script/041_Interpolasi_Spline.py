import numpy as np
import scipy.interpolate as interpolasi
import matplotlib.pyplot as plt
import time

start = time.time()
data = np.genfromtxt('gammaray.txt')
kedalaman = data[:, 0]
data_Gamma_Ray = data[:, 5]

x = kedalaman
y = data_Gamma_Ray

kedalaman_1 = np.linspace(kedalaman[0], kedalaman[14], num=100)

# Interpolasi Linear
Gamma_RSP_1 = interpolasi.interp1d(kedalaman[0:15], data_Gamma_Ray[0:15], kind='linear')
Gamma_Ray_1 = Gamma_RSP_1(kedalaman_1)

# Interpolasi Quadratic
Gamma_RSP_2 = interpolasi.interp1d(kedalaman[0:15], data_Gamma_Ray[0:15], kind='quadratic')
Gamma_Ray_2 = Gamma_RSP_2(kedalaman_1)

# Interpolasi Cubic
Gamma_RSP_3 = interpolasi.interp1d(kedalaman[0:15], data_Gamma_Ray[0:15], kind='cubic')
Gamma_Ray_3 = Gamma_RSP_3(kedalaman_1)

# Plot Interpolasi Linear
plt.subplot(141)
plt.plot(y[0:14], x[0:14], 'db')
plt.plot(Gamma_Ray_1, kedalaman_1, 'b')
plt.gca().invert_yaxis()
plt.xlabel("Gamma Ray")
plt.ylabel("Depth (m)")
plt.title("Linear Spline")

# Plot Interpolasi Quadratic
plt.subplot(142)
plt.plot(y[0:14], x[0:14], 'og')
plt.plot(Gamma_Ray_2, kedalaman_1, 'g')
plt.gca().invert_yaxis()
plt.xlabel("Gamma Ray")
plt.title("Quadratic Spline")

# Plot Interpolasi Cubic
plt.subplot(143)
plt.plot(y[0:14], x[0:14], 'or')
plt.plot(Gamma_Ray_3, kedalaman_1, 'r')
plt.gca().invert_yaxis()
plt.xlabel("Gamma Ray")
plt.title("Cubic Spline")

# Menampilkan semua grafik
plt.suptitle("Perbandingan Grafik Spline (Linear, Quadratic, dan Cubic)")
plt.show()
