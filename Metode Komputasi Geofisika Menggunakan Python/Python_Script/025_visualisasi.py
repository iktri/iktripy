# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 361, 10)
# y = np.sin(x * np.pi / 180)
#
# plt.plot(x, y, color='b', linewidth='2', alpha=0.8)
# plt.xlabel('Sudut (deg)')
# plt.ylabel('Sin')
# plt.xlim(0, 360)
# plt.ylim(-1, 1)
# plt.grid('True')
# plt.show()
#
# # Inverse axis
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0,1001,10)
# z = np.arange(0,10001,100)
# plt.plot(x,z)
# plt.gca().invert_yaxis()
# plt.show()
#
# # Overlay dua kurva
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 361, 10)
# a = np.sin(x * np.pi / 180)
# b = np.cos(x * np.pi / 180)
#
# plt.plot(x, a, '--go', x, b, ':r*')
# plt.xlabel('Sudut (deg)')
# plt.xlim(0, 360)
# plt.ylim(-1, 1)
# plt.show()
#
# # Contoh plotting stem
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 361, 10)
# a = np.sin(x * np.pi / 180)
# b = np.cos(x * np.pi / 180)
#
# plt.stem(x, a, linefmt='red', markerfmt='D')
# plt.stem(x, b)
#
# plt.plot(x, a+b, color='b', linewidth='2', alpha=0.8)
# plt.xlabel('Sudut (deg)')
# plt.xlim(0, 360)
# plt.grid('True')
# plt.show()
#
# # Menambahkan legend
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 361, 10)
# a = np.sin(x * np.pi / 180)
# b = np.cos(x * np.pi / 180)
#
# plt.stem(x, a, linefmt='red', markerfmt='D', label='sin(x)')
# plt.stem(x, b, label='cos(x)')
# plt.plot(x, a+b, color='b', linewidth='2', alpha=0.8, label='sin(x) + cos(x)')
#
# plt.legend(loc='upper right', shadow=True, fontsize='x-large')
# plt.xlabel('Sudut (deg)')
# plt.xlim(0, 360)
# plt.grid('True')
# plt.show()
#
# # Contoh untuk menunjukkan area
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 360)
# a = np.sin(x * np.pi / 180)
# b = np.cos(x * np.pi / 180)
#
# plt.plot(x, a, color='b', linewidth='2', alpha=0.8)
# plt.plot(x, b, color='r', linewidth='2', alpha=0.8)
# plt.fill_between(x, a, color='b', alpha=0.4)
# plt.fill_between(x, b, color='r', alpha=0.4)
# plt.xlabel('Sudut (deg)')
# plt.xlim(0, 360)
# plt.show()
#
# #Menampilkan histogram
# import matplotlib.pyplot as plt
#
# ipk = [3.88, 3.54, 2.87, 3.24, 1.67, 2.11, 3.87, 1.01, 2.08,
#        1.88, 3.98, 2.76, 3.50, 4.00, 0.54, 2.89, 3.17, 1.33,
#        2.48, 2.22]
#
# plt.hist(ipk, bins=[0,1,2,3,4], facecolor='g')
# plt.xlabel('IPK')
# plt.ylabel('Jumlah Mahasiswa')
# plt.show()
#
# # Contoh membuat subplot
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 361, 10)
# a = np.sin(x * np.pi / 180)
# b = np.cos(x * np.pi / 180)
#
# fig = plt.figure()
# ax1 = fig.add_subplot(121)
# ax1.plot(x, a, color='b', linewidth='2', alpha=0.8)
# ax1.grid(True)
# ax1.set_xlabel('Sudut (Deg)')
# ax1.set_ylabel('sin(x)')
# ax1.set_title('sin(x)')
#
# ax2 = fig.add_subplot(122)
# ax2.plot(x, b, color='r', linewidth='2', alpha=0.8)
# ax2.grid(True)
# ax2.set_xlabel('Sudut (Deg)')
# ax2.set_ylabel('cos(x)')
# ax2.set_title('cos(x)')
#
# plt.show()
#
# # Contoh lain
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 361, 10)
# a = np.sin(x * np.pi / 180)
# b = np.cos(x * np.pi / 180)
#
# plt.subplot(211)
# plt.plot(x, a, color='b', linewidth='2', alpha=0.8)
# plt.grid(True)
# plt.xlabel('Sudut (Deg)')
# plt.ylabel('sin(x)')
# plt.title('sin(x)')
#
# plt.subplot(212)
# plt.plot(x, b, color='r', linewidth='2', alpha=0.8)
# plt.grid(True)
# plt.xlabel('Sudut (Deg)')
# plt.ylabel('cos(x)')
# plt.title('cos(x)')
#
# plt.show()
#
# # Contoh plotting 3D
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# x = np.arange(0,361,10)
# y = np.arange(0,361,10)
# b = np.cos(x*np.pi/180)
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(x, y, b)
# plt.show()
#
# # Contoh plotting 3D scatter:
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# zdata = 15 * np.random.random(100)
# xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
# ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# cdata = zdata
#
# ax.scatter(xdata, ydata, zdata, c=cdata, cmap='rainbow')
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# plt.show()
#
# # Contoh plotting 3D wireframe:
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
#
# points = np.linspace(-2, 2, 20)
# [x, y] = np.meshgrid(points, points)
# # plt.plot(x,y)  # Baris ini dikomentari di gambar
#
# z = (2 / (np.exp((x - 0.5)**2 + (y + 2)**2))) - (2 / (np.exp((x + 0.5)**2 + (y**2))))
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_wireframe(x_
#
# # Contoh plotting 3D surface:
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
#
# points = np.linspace(-2, 2, 20)
# [x, y] = np.meshgrid(points, points)
# z = (2 / (np.exp((x - 0.5)**2 + (y + 2)**2))) - (2 / (np.exp((x + 0.5)**2 + (y**2))))
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# cbar = ax.plot_surface(x, y, z, cmap='jet')
# fig.colorbar(cbar)
# plt.show()
#
# # Contoh plotting kontur
# from mpl_toolkits.mplot3d import axes3d
# import matplotlib.pyplot as plt
# import numpy as np
#
# points = np.linspace(-2, 2, 20)
# [x, y] = np.meshgrid(points, points)
# z = (2 / (np.exp((x - 0.5)**2 + (y + 2)**2))) - (2 / (np.exp((x + 0.5)**2 + (y**2))))
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.contour(x, y, z, cmap='jet')
# plt.show()
