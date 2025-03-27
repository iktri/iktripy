        # Cara mengetahui kapasitas file
# import os
# f = open("018_test.txt")
# print(os.stat("018_test.txt").st_size)

        # Open a file
# f = open("018_test.txt")
# # open file in current directory
# f = open("C:/Python33/README.txt")  # specifying full path

# f = open("018_test.txt")
# # equivalent to 'r' or 'rt'
# f = open("018_test.txt",'w')  # write in text mode

        # # Close a file
# f = open("018_test.txt")
# # perform file operations
# f.close()

# with open("018_test.txt") as f:
# # perform file operations

#         # Write a File
# with open("018_test.txt",'w') as f:
#     f.write("my first file\n")
#     f.write("This file\n\n")
#     f.write("contains three lines\n")

#         # Read a file
# f = open("angka.txt",'r')
# print(f.read(4))
# # read the first 4 data

#         # Save data
# import numpy as np
# x = np.linspace(-4,4,81)
# y = np.sinc(x)
# print(x)
# data = np.vstack((x,y)).T
# np.save('./data',data)
# np.savetxt('./data.txt',data)

#         # Load data
# import numpy as np
# data = np.load('./data.npy')
# data = np.load('./data.txt')

# import numpy as np
# data = np.genfromtxt('018_test.txt')
# NIM = data[:, 0]
# Nama = data[:, 1]
# Nilai = data[:, 2]

#         # Dalam format csv
# import csv
#
# with open('018_test.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=' ')
#     x = []
#     y = []
#     z = []
#     for row in csv_reader:
#             x.append(row[0])
#             y.append(row[1])
#             z.append(row[2])
# print(x)
# print(y)
# print(z)
#
# import pandas as pd
#
# tes = pd.read_csv('018_test.txt')
# print(tes.head())
# print(tes.columns)

        # # Input value
# val = float(input("Enter your value: "))
# print(val)
# print(val/5)

# while True:
#     val = float(input("Enter your value: "))
#     print("You got",val/5)
#     option = input("Again?(y/n) ")
#     if option == 'n':
#         break

