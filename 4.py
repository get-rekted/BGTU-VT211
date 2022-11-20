# Вычислить скалярное произведение двух векторов

import numpy as np

# Ввод данных
print('Первый вектор')
a = [int(x) for x in input().split()]
print('Второй вектор')
b = [int(x) for x in input().split()]

A = np.array(a)
B = np.array(b)

# Решение
res = np.dot(A, B, out=None)

# Вывод результата
print(res)