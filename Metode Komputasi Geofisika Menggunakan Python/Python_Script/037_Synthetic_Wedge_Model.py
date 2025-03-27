# import numpy as np
# import matplotlib.pyplot as plt
#
# # ---------------- DEFINE MODELING PARAMETERS HERE ----------------
# # 3-Layer Model Parameters (Layer1, Layer2, Layer3)
# vp_mod = [2500.0, 2600.0, 2550.0]  # P-wave velocity (m/s)
# vs_mod = [1200.0, 1300.0, 1200.0]  # S-wave velocity (m/s)
# rho_mod = [1.95, 2.0, 1.98]        # Density (g/cc)
#
# dz_min = 0.0   # Minimum thickness of Layer 2 (m)
# dz_max = 60.0  # Maximum thickness of Layer 2 (m)
# dz_step = 1.0  # Thickness step from trace-to-trace (normally 1.0 m)
#
# # Kondisi apabila ketiga lapisan dibatasi time tertentu
# pada time tertentu.
# vp = [2500, 2600, 2550]
# rho = [1950, 2000, 1980]
#
# rc = []
# for i in range(0, 2):
#     ref = ((rho[i+1] * vp[i+1]) - (rho[i] * vp[i])) / ((rho[i+1] * vp[i+1]) + (rho[i] * vp[i]))
#     rc.append(ref)
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Ricker wavelet
# l = 400   # wavelet length (ms)
# s = 4     # sampling rate (ms)
# f = 25    # frequency (Hz)
# t = np.arange(-l/2000, l/2000+s/1000, s/1000)  # must be in seconds
# r = (1 - 2 * np.pi**2 * f**2 * t**2) * np.exp(-1 * np.pi**2 * f**2 * t**2)  # Ricker wavelet
#
# plt.plot(t, r)
# plt.show()
#
# tr = 0.0 * np.arange(0, len(r), 1)
# tr[30] = rc[0]
# tr[60] = rc[1]
# times = np.arange(0, len(r) + len(tr) - 1, 1)
# for i in range(50):
#     seismic = np.convolve(r,tr)
#     plt.plot(seismic+i*0.02,time,'r-')
#     plt.ylim(max(time),min(time))
#     plt.ylabel('time(ms)')
# plt.show()
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 3-Layer Model Parameters [Layer1, Layer2, Layer 3]
# vp_mod = [2500.0, 2600.0, 2550.0]  # P-wave velocity (m/s)
# vs_mod = [1200.0, 1300.0, 1200.0]  # S-wave velocity (m/s)
# rho_mod = [1.95, 2.0, 1.98]        # Density (g/cc)
#
# dz_min = 0.0   # Minimum thickness of Layer 2 (m)
# dz_max = 60.0  # Maximum thickness of Layer 2 (m)
# dz_step = 1.0  # Thickness step from trace-to-trace (normally 1.0 m)
#
# # Plot Parameters
# min_plot_time = 0.15
# max_plot_time = 0.3
#
# def calc_times(z_int, vp_mod):
#     t_int = []
#     nlayers = len(vp_mod)
#     nint = nlayers - 1
#
#     for i in range(0, nint):
#         if i == 0:
#             tbuf = 2.0 * z_int[i] / vp_mod[i+1]
#             t_int.append(tbuf)
#         else:
#             zdiff = z_int[i] - z_int[i-1]
#             tbuf = 2.0 * zdiff / vp_mod[i+1] + t_int[i - 1]
#             t_int.append(tbuf)
#
#     return t_int
#
# nmodel = int((dz_max - dz_min) / dz_step + 1)
#
# lyr_times = []
# for model in range(0, nmodel):
#     # Calculate interface depths
#     z_int = [500.0]
#     z_int.append(z_int[0] + dz_min + dz_step * model)
#
#     # Calculate interface times
#     t_int = calc_times(z_int, vp_mod)
#     lyr_times.append(t_int)
#
# lyr_times = np.array(lyr_times)
#
# plt.plot(lyr_times[:, 0], color='blue', lw=1.5)
# plt.plot(lyr_times[:, 1], color='red', lw=1.5)
# plt.xlim(min_plot_time, max_plot_time)
# plt.gca().invert_xaxis()
# plt.xlabel("Thickness (m)")
# plt.ylabel("Time (s)")
# plt.text(1, min_plot_time + (lyr_times[0, 0] - min_plot_time) / 2., "Layer 1",
#          fontsize=16)
#
# plt.text(dz_max / dz_step - 2,
#          lyr_times[-1, 0] + (lyr_times[-1, 1] - lyr_times[-1, 0]) / 2.,
#          "Layer 2", fontsize=16, horizontalalignment='right')
#
# plt.text(2,
#          lyr_times[0, 0] + (max_plot_time - lyr_times[0, 0]) / 2.,
#          "Layer 3", fontsize=16)
#
# plt.gca().xaxis.tick_top()
# plt.gca().xaxis.set_label_position('top')
# plt.show()
#
# # Jika wavelet bukan 0
# import matplotlib.pyplot as plt
#
# # Ricker Wavelet Parameters
# wvlt_length = 0.128
# wvlt_cfreq = 30.0
# wvlt_phase = 0.0
# dt = 0.0001
#
#
# def ricker(cfreq, phase, dt, wvlt_length):
#     import numpy as np
#     import scipy.signal as signal
#
#     nsamp = int(wvlt_length / dt + 1)
#     t_max = wvlt_length / 2
#     t_min = -t_max
#
#     t = np.arange(t_min, t_max, dt)
#
#     wvlt = np.linspace(-wvlt_length / 2, (wvlt_length - dt) / 2, wvlt_length / dt)
#     wvlt = (1.0 - 2.0 * (np.pi * cfreq * t) ** 2) * (cfreq ** 2) * (t ** 2) * \
#            np.exp(-np.pi * (cfreq ** 2) * (t ** 2))
#
#     if phase != 0:
#         phase = phase * np.pi / 180.0
#         wvlt_h = signal.hilbert(wvlt)
#         wvlt_r = np.imag(wvlt_h)
#
#         wvlt = np.cos(phase) * wvlt - np.sin(phase) * wvlt_r
#
#     return t, wvlt
# #   Generate ricker wavelet
# wvlt_t, wvlt_amp = ricker(wvlt_cfreq, wvlt_phase, dt, wvlt_length)
# plt.plot(wvlt_t,wvlt_amp,'k-')
# plt.title('Ricker Wavelet')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.ylim(-1,1.5)
# plt.show()
#
# # koef RC jika diketahui v dan p setiap lapisan
# # 3-Layer Model Parameters [Layer1, Layer2, Layer 3]
# vp_mod = [2500.0, 2600.0, 2550.0]  # P-wave velocity (m/s)
# rho_mod = [1.95, 2.0, 1.98]  # Density (g/cc)
#
# def calc_rc(vp_mod, rho_mod):
#     '''
#     rc_int = calc_rc(vp_mod, rho_mod)
#     '''
#
#     nlayers = len(vp_mod)
#     nint = nlayers - 1
#
#     rc_int = []
#
#     for i in range(0, nint):
#         buf1 = vp_mod[i + 1] * rho_mod[i + 1] - vp_mod[i] * rho_mod[i]
#         buf2 = vp_mod[i + 1] * rho_mod[i + 1] + vp_mod[i] * rho_mod[i]
#         buf3 = buf1 / buf2
#         rc_int.append(buf3)
#
#     return rc_int
#
# # Calculate reflectivities from model parameters
# rc_int = calc_rc(vp_mod, rho_mod)
#
# print(rc_int)
#
# #  kemudian di-digitasi
# def digitize_model(rc_int, t_int, t):
#     """
#     rc = digitize_model(rc, t_int, t)
#
#     rc = Reflection coefficients corresponding to interface times
#     t_int = interface times
#     t = regularly sampled time series defining model sampling
#     """
#
#     import numpy as np
#
#     nlayers = len(rc_int)
#     nint = nlayers - 1
#     nsamp = len(t)
#
#     rc = list(np.zeros(nsamp, dtype="float"))
#     lyr = 0
#
#     for i in range(0, nsamp):
#         if t[i] >= t_int[lyr]:
#             rc[i] = rc_int[lyr]
#             lyr = lyr + 1
#
#         if lyr > nint:
#             break
#
#     return rc
#
#
# # Trace Parameters
# tmin = 0.0
# tmax = 0.5
# dt = 0.0001  # changing this from 0.0001 can affect the display quality
#
# zc = 0.0
# rc_zo = []
#
# for model in range(0, 1):
#     # Calculate interface depths
#     t_int = [500.0]
#     dz_int = 0.1
#     z_int.append(zc + dz_int * model)
#
#     # Calculate interface times
#     t_int = calc_times(z_int, vp_mod)
#
#     # Digitize 3-layer model
#     nsamp = int((tmax - tmin) / dt) + 1
#     t = []
#     for i in range(0, nsamp):
#         t.append(i * dt)
#
#     rc = digitize_model(rc_int, t_int, t)
#     rc_zo.append(rc)
#
# # Lalu  konvolusi antara koefisien refleksi (rc) dan Ricker wavelet
# syn_zo = []
#
# for model in range(0, nmodels):
#     syn_buf = np.convolve(rc, wlt_amp, mode='same')
#     syn_buf = list(syn_buf)
#     syn_zo.append(syn_buf)
#
# syn_zo = np.array(syn_zo)
# t = np.array(t)
#
#
# # Fungsi untuk mem-visualisasikan konvolusi tersebut adalah:
#
# # Plot Parameters
# min_plot_time = 0.15
# max_plot_time = 0.3
# excursion = 2
#
# [ntrc, nsamp] = syn_zo.shape
#
# def plot_wig(axhdl, data, t, excursion, highlight=None):
#     import numpy as np
#     import matplotlib.pyplot as plt
#
#     [ntrc, nsamp] = data.shape
#
#     t = np.hstack([0, t, t.max()])
#
#     for i in range(0, ntrc):
#         tbuf = excursion * data[i] / np.max(np.abs(data)) + i
#         tbuf = np.hstack([i, tbuf, i])
#
#         if i == highlight:
#             lw = 0.5
#         else:
#             lw = 1.0
#
#         axhdl.plot(tbuf, t, color='black', linewidth=lw)
#
#         plt.fill_between(t, tbuf, i, where=tbuf > i, facecolor=[0.6, 0.6, 1.0], linewidth=0)
#         plt.fill_between(t, tbuf, i, where=tbuf < i, facecolor=[1.0, 0.7, 0.7], linewidth=0)
#     axhdl.set_xlim(-excursion, ntrc + excursion)
#     axhdl.xaxis.tick_top()
#     axhdl.xaxis.set_label_position('top')
#     axhdl.invert_yaxis()
#
# fig = plt.figure(figsize=(12, 14))
# ax1 = fig.add_subplot(1, 1, 1)
# plot_wig(ax1, syn_zo, t, excursion)
#
# ax1.plot([i insetion], [0], color='blue', lw=1.5)
# ax1.plot([lyr times], [i], color='red', lw=1.5)
#
# ax1.set_ylim(min_plot_time, max_plot_time)
# ax1.invert_yaxis()
# ax1.set_xlabel('Thickness (m)')
# ax1.set_ylabel('Time (s)')
#
# plt.show()
#
# # Posisi digit layer pada setiap trace disimpan dalam array lyr_index
# lyr_index = np.array(np.round(lyr_times / dt), dtype='int16')
#
# # Langkah berikutnya adalah menentukan tuning thickness,
# # yaitu dengan mencari posisi trace yang memiliki nilai amplitude tertinggi.
# tuning_trace = np.argmax(np.abs(syn_zo.T)) % syn_zo.T.shape[1]
# tuning_thickness = tuning_trace * dz_step
#
# plt.plot(syn_zo[:, lyr_index[:, 0]], color='blue')
# plt.xlim(-excursion, ntrc + excursion)
# plt.axvline(tuning_trace, color='k', lw=2)
# plt.grid()
# plt.title('Upper interface amplitude')
# plt.xlabel('Thickness (m)')
# plt.ylabel('Amplitude')
# plt.text(tuning_trace + 2, plt.ylim()[0] * 1.1,
#          'Tuning thickness = {0} m'.format(tuning_thickness),
#          fontsize=16)
# plt.show()
