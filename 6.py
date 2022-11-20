# Вычислить смешанное произведение трех векторов

import numpy as np

# Ввод трех векторов
a = [int(x) for x in input('первый: ').split()]
b = [int(x) for x in input('второй: ').split()]
c = [int(x) for x in input('третий: ').split()]

# a = [4, 10, 8]
# b = [5, 1, 9]
# c = [7, 2, 3]

# Векторное произведение
zv = np.cross(b, c)

# Скалярное произведение
edn = np.dot(a, zv, out=None)

# Результат
print('\nВекторное произведение равно:',zv)
print('\nСкалярное произведение равно:',edn)