# import PyOSGPUP.segypy as segypy
# import matplotlib.pyplot as plt
# from scipy.fftpack import fft
# import numpy as np
#
# # Read Segy File
# [data, SH, STH] = segypy.readSegy('shotgather.sgy')
#
# plt.subplot(211)
# seismic = data[:, 7]
# plt.plot(seismic)
# plt.title("Fast Fourier Transform")
# plt.xlabel("Time(ms)")
# plt.ylabel("Amplitude")
# plt.grid()
#
# # fft
# T = 0.004
# Fs = 1 / T
# L = len(seismic)
# Y = fft(seismic)
# P1 = np.abs(Y / L)
# P2 = P1[0:int(L / 2)]
# f = Fs * np.arange(0, int(L / 2)) / L
#
# plt.subplot(212)
# plt.plot(f, P2)
# plt.xlabel(" Frequency (Hz)")
# plt.ylabel("Amplitude")
# plt.show()