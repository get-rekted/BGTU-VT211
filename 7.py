# Вычислить угол между двумя заданными векторами

import numpy as np

# Ввод векторов
a = [int(x) for x in input('первый вектор: ').split()]
b = [int(x) for x in input('второй вектор: ').split()]

# Решение
cos_angle = np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)

# Вывод результата
print('угол между векторами А и Б равен: ', cos_angle)
print('угол равен: ', np.arccos(cos_angle))
