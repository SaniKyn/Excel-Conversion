import pandas as pd
import numpy as np
import math

df = pd.read_excel('test.xlsx', sheet_name='Лист1')


def truncated_data(y):
    k = []
    avg_y = np.mean(y)
    abs_val_minus_avg = abs(y - avg_y)
    for i in abs_val_minus_avg:
        if avg_y < i:
            k.append(abs_val_minus_avg)
    norm_values = sorted(y)[:-len(k)]
    average_value_common_k = np.sum(norm_values) / (len(y) - len(k))
    return average_value_common_k, norm_values


def work_data(average, n):
    sum_n = math.sqrt(np.sum(((n - average) ** 2) / len(n)))
    return sum_n


def result_six_sigma(avck, y, s):
    for i in sorted(y):
        if abs(i - avck) > s:
            print(i, 'Грубая ошибка')


avck, norm = truncated_data(df['y'])
s = work_data(avck, norm) * 6
result_six_sigma(avck, df['y'], s)
