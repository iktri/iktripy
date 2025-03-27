import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file
data = np.genfromtxt('gammaray.txt')
depth = data[0:100, 0]  # Kedalaman
gammaray = data[0:100, 5]  # Data Gamma Ray
order = 5  # Orde Moving Average

# Fungsi Moving Average
def movingaverage(values, periode):
    mean = np.repeat(1.0, periode) / periode
    sma = np.convolve(values, mean, 'valid')  # Perhitungan Moving Average
    return sma

# Menghitung Moving Average untuk kedalaman dan Gamma Ray
MV_Depth = movingaverage(depth, order)
MV_Gammaray = movingaverage(gammaray, order)

# Plot hasil data asli dan hasil Moving Average
plt.plot(MV_Gammaray, MV_Depth, color='blue', label='Grafik Hasil Moving Average')
plt.plot(gammaray, depth, 'o', color='red', label='Data Gamma Ray')

plt.gca().invert_yaxis()
plt.xlabel("Gamma Ray (API)")
plt.ylabel("Depth (m)")
plt.legend()
plt.title("Smoothing 1D dengan Moving Average data Gamma Ray")
plt.show()
