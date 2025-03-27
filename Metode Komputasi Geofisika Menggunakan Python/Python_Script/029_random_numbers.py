# import random as rd
# for i in range(10):
#     print(rd.random())
#
# import random as rd
# names = ['a','b','c']
# for i in range(1):
#     print(rd.choice(names))
#
# import random as rd
#
# noise = []
# for i in range(360):
#     noise.append(0.1 * rd.random())
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 360)
# y = np.sin(x * np.pi / 180)
#
# plt.subplot(1, 2, 1)
# plt.plot(x, noise, color='r')
# plt.xlabel('Sudut (Deg)')
# plt.ylabel('noise')
# plt.xlim(0, 360)
# plt.ylim(-1, 1)
#
# plt.subplot(1, 2, 2)
# plt.plot(x, y + noise, color='r')
# plt.xlabel('Sudut (Deg)')
# plt.ylabel('signal')
# plt.xlim(0, 360)
# plt.ylim(-1, 1)
#
# plt.show()
