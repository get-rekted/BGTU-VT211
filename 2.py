# Решить СЛАУ с n-неизвестными, методом Гаусса

import numpy as np

# Матрица
A = np.array([[2., 5.], [1., -10.]])
# Вектор
B = np.array([1., 3.])

# Решение
x = np.linalg.solve(A, B)

# Вывод ответа в консоль
print(x)
