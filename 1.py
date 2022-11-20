# Вычислить определитель матрицы размера n/n путем преобразования

import numpy as np

print('''введите данные как указано в примере
!!! ! !!!
пример: -4 -1 2; 10 4 -1; 8 3 1, это матрица вида [-4 -1 2] [10 4 -1] и т.д.''')

# Ввод
mat = input('Type it: ')

# Вычисления
a = np.matrix(mat)
b = np.linalg.det(a)

# Вывод решения
print('Матрица: \n', a)
print('\Решение: ', b)
