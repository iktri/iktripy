# import numpy as np
# from scipy.sparse.linalg import lsqr
#
# data = np.genfromtxt('032_data_bvalue.dat')
# magnitude = data[:, 0]
# frequency = data[:, 1]
# M = np.array(magnitude)
# logN = np.array(np.log10(frequency))
# M = np.column_stack((M, np.ones(np.shape(M)[0])))
# grad = lsqr(M, logN)[0]
# a = grad[1]
# b = grad[0]*-1
#
# print('a-value is: ', '%.2f' %a)
# print('b-value is: ', '%.2f' %b)
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# # data awal
# data = np.genfromtxt('032_data_bvalue.dat')
# x = data[:, 0]
# y = data[:, 1]
#
# # nilai a dan b-value
# p = np.polyfit(x, np.log10(y), 1)
# print('Least Square : b value: ', '%.2f' % -p[0], ' a value: ', '%.2f' % p[1])
#
# # perbandingan data awal vs regresi
# y_akhir = 10**(p[0]*x + p[1])
# plt.plot(x, np.log10(y), 'ko', label='Data', color='indigo')
# plt.plot(x, np.log10(y_akhir), label='Regresi', color='cyan')
# plt.xlabel('Magnitudo')
# plt.ylabel('Log N')
# plt.legend()
# plt.title('Data VS Regresi')
# plt.show()
