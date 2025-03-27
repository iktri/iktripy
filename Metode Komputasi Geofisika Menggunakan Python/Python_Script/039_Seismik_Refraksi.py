# # Script first break picking
#
# from scipy.sparse.linalg import laqr
#
# offset = 50 * y
# plt.plot(x, offset, 'r.')
# fig = plt.ginput(1)
# fig.suptitle('Data Picking')
# plt.ylabel('Time (s)')
# plt.xlabel('Offset (m)')
# print("Select two slopes (start-end points)")
# slope = plt.ginput(4)
# print("Slope:", slope)
# plt.show()
#
# # Ketebalan lapisan
# np.savetxt('slope.txt', result, fmt='%.4f')
# dfz = np.genfromtxt('slope.txt')
#
# time = dfz[:, 0]
# offset = dfz[:, 1]
#
# V1 = (offset[1] - offset[0]) / (time[1] - time[0])
# V2 = (offset[3] - offset[2]) / (time[3] - time[2])
#
# x_lin = np.array([time[1], time[3]])
# y_lin = np.array([offset[1], offset[3]])
# x_lin = np.column_stack([x_lin, np.ones(np.shape(x_lin)[0])])
# grad = np.linalg.lstsq(x_lin, y_lin, rcond=None)[0]
#
# t1 = grad[1]
#
# h1 = (t1 / 2) * (((1/V1)**2) - ((1/V2)**2))**0.5
#
# print("Kecepatan lapisan pertama =", V1, "m/s")
# print("Kecepatan lapisan kedua =", V2, "m/s")
# print("Ketebalan lapisan pertama =", h1, "m")
#
