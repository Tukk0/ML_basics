# Реализуйте функцию most_frequent, принимающую на вход массив целых неотрицательных чисел nums и возвращающую самый частый элемент массива.

import pandas as pd

def most_frequent(nums):
    nums_series = pd.Series(nums)
    return nums_series.mode()[0]
