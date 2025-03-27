# # Contoh perhitungan regresi linear pada Python adalah:
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([1, 3, 2, 5, 7, 8, 9, 10, 12, 13])
#
# m_x, m_y = np.mean(x), np.mean(y)
#
# SS_xy = np.sum((x - m_x) * (y - m_y))
# SS_xx = np.sum((x - m_x) ** 2)
# SS_yy = np.sum((y - m_y) ** 2)
#
# b = SS_xy / SS_xx
# a = m_y - b * m_x
#
# print(a, b)
#
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
#
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# y = np.array([1, 3, 2, 5, 7, 8, 9, 10, 12, 13])
#
# model = LinearRegression().fit(x, y)
# r_sq = model.score(x, y)
# print(r_sq)
#
# print('intercept', model.intercept_)
# print('gradient', model.coef_)
#
# y_pred = model.predict(x)
#
# plt.scatter(x, y)
# plt.plot(x, y_pred, 'g')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
