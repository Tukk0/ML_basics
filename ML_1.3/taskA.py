'''
Реализуйте функцию construct_matrix, принимающую на вход два одномерных массива x и y и возвращающую матрицу, в которой первый массив соответствует первому столбцу матрицы, второй — второму.

В качестве решения предоставьте код функции, вызывать ее не требуется.
'''

import numpy as np

def construct_matrix(first_array, second_array):
    return np.dstack([first_array, second_array]).reshape([-1,2])
