# Вычислить обратную матрицу для заданной, используя решение СЛАУ

import numpy as np

# Матрица
A = np.array([[3, 1], [1, 2]])

# Вектор
B = np.array([9, 8])

# Вычислим определитель 
A_det = np.linalg.det(A)

# Вычислим обратную матрицу
A_inv = np.linalg.inv(A)

# Конечное решение
A_fin = np.linalg.solve(A, B)

def main():
    if A_det == 0:
        print('Определитель равен 0!')
    else:
        print('\nМатрица\n', A)
        print('\nОпределитель:\n', A_det)
        print('\nОпределитель не равен 0, решение есть')
        print('\nОбратная матрица\n', A_inv)
        print('\nИтоговый результат\n', A_fin)

main()