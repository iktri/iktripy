import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file
cr = np.genfromtxt('channel.txt')
traces = []

# Parameter Ricker Wavelet
L = 400  # Panjang wavelet (ms)
s = 4    # Sampling rate (ms)
f = 25   # Frekuensi (Hz)

# Waktu dalam detik
t = np.arange(-L/2000, L/2000 + s/1000, s/1000)

# Persamaan Ricker Wavelet
ricker = (1 - 2 * np.pi**2 * f**2 * t**2) * np.exp(-1 * np.pi**2 * f**2 * t**2)

# Proses konvolusi untuk setiap trace
for i in range(cr.shape[1]):
    seismic = np.convolve(ricker, cr[:, i], 'same')  # Konvolusi sinyal
    traces.append(seismic)

# Mengubah daftar menjadi array NumPy
traces = np.asarray(traces).T

# Menambahkan noise ke data
noise = 0.3 * np.random.random((traces.shape[0], traces.shape[1]))
traces_noisy = traces + noise

# Menampilkan hasil dengan peta warna seismik
plt.imshow(traces_noisy, cmap='seismic', vmin=-0.8, vmax=0.7, interpolation='bilinear')
plt.show()

# Menyimpan hasil ke file
np.save('traces', traces_noisy)
