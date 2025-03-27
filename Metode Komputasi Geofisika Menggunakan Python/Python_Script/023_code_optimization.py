# import time
#
# # Slower
# start1 = time.time()
# a = range(100000)
# b = []
# for i in a:
#     b.append(i * 2)
# end1 = time.time()
# print(end1 - start1)
#
# # Faster
# start2 = time.time()
# a = range(100000)
# b = [i * 2 for i in a]
# end2 = time.time()
# print(end2 - start2)

# import time
# import numpy as np

# # Slower
# start1 = time.time()
# a = range(100000)
# b = np.zeros(len(a))
# for i in a:
#     b[i] = i * 2
# end1 = time.time()
# print(end1 - start1)
#
# # Faster
# start2 = time.time()
# a = range(100000)
# b = []
# for i in a:
#     b.append(i * 2)
# end2 = time.time()
# print(end2 - start2)

# # Contoh lain
# # slower
# x = 2
# y = 5
# temp = x
# x = y
# y = temp
# print(x, y)
#
# # faster
# x, y = 2, 5
# x, y = y, x
# print(x, y)

my_var = 'you'

# # slow
# msg = 'hello ' + my_var + ' world'
# print(msg)
#
# # fast
# msg = 'hello %s world' % my_var
# print(msg)
#
# # faster
# msg = 'hello {} world'.format(my_var)
# print(msg)

# # slow
# msg = 'line1\n'
# msg += 'line2\n'
# msg += 'line3\n'
# print(msg)
#
# # fast
# msg = ['line1', 'line2', 'line3']
# s = '\n'
# print(s.join(msg))
