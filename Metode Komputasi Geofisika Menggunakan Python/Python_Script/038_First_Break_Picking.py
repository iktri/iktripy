# import PVGeo.gslib as segypy
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Read SEGY File
# [data, SH, SHH] = segypy.readSegy('shot.sgy')
# print(SH)  # SEGY header data [50 x 2590]
#
# if 'time' in SH:
#     time = SH['time']  # time
#     ntraces = SH['ntraces']  # trace count
#     ns = SH['ns']  # number of samples
# else:
#     ns = data.shape[0]
#     time = np.arange(ns)
#     ntraces = data.shape[1]
#
# print("Number of traces:", ntraces)
# print("Record length:", ns-1, "ms")
#
# # Plot
# maxval = -1
# if maxval < 0:
#     maxval = np.max(data)
# maxval = 1.1 * maxval / 0.1
#
# fig = plt.figure(figsize=(10, 5))
# for i in range(0, 255, 5):
#     trace = data[:, i] - i
#     plt.plot(trace/maxval, time, color='b', linewidth=1, picker=10)
#
#     for n in range(len(trace)):
#         if trace[n] < 0:
#             plt.fill_betweenx(time, trace, 'r', linewidth=1)
#
# plt.grid(True)
# plt.gca().invert_yaxis()
# plt.xlabel('Trace number')
#
# if 'time' in SH:
#     plt.ylabel('Time (ms)')
# else:
#     plt.ylabel('Sample number')
#
# if 'filename' in SH:
#     plt.title(SH['filename'])
# else:
#     plt.title('SEGY File')
#
# print("Pick by clicking the first arrival time of every trace")
# plt.show()
#
# plt.ginput(n=1, mouse_add=1, mouse_pop=3, mouse_stop=2)
# print("Result:", result)
#
# # Simpan ke format ASCII
# np.savetxt('picking.txt', result, fmt='%.4f')
# dt = np.genfromtxt('picking.txt')
# x = dt[:,0]
# y = dt[:,1]