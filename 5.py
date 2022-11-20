# Вычислить векторное произведение двух векторов

import numpy as np

# Ввод данных
a = [int(x) for x in input('первый вектор: ').split()]
b = [int(x) for x in input('второй вектор: ').split()]

A = np.array(a)
B = np.array(b)

# Решение
res = np.cross(A, B)

# Вывод ответа
print(res)