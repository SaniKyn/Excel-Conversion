import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_excel('test.xlsx', sheet_name='Лист1')


# Находит критическое значение с учётом объёма выборки и уровня значимости
def calculate_critical_value(size, alpha):
    t_dist = stats.t.ppf(1 - alpha / (2 * size), size - 2)
    numerator = (size - 1) * np.sqrt(np.square(t_dist))
    denominator = np.sqrt(size) * np.sqrt(size - 2 + np.square(t_dist))
    critical_value = numerator / denominator
    print(f"Критическое значение Граббса: {critical_value}")
    return critical_value


# Находит значение критерия Граббса и максимальное значение в наборе данных
def grubbs_stat(y):
    std_dev = np.std(y)
    avg_y = np.mean(y)
    abs_val_minus_avg = abs(y - avg_y)
    max_of_deviations = max(abs_val_minus_avg)
    max_ind = np.argmax(abs_val_minus_avg)
    Gcal = max_of_deviations / std_dev
    print(f"Значение критерия Граббса: {Gcal}")
    return Gcal, max_ind


# Является ли значение с максимальным индексом выбросом
def check_G_values(Gs, Gc, inp, max_index):
    if Gs > Gc:
        print(f"{inp[max_index]} является выбросом")
    else:
        print(f"{inp[max_index]} это не выброс")


Gcritical = calculate_critical_value(len(df['y']), 0.05)
Gstat, max_index = grubbs_stat(df['y'])
check_G_values(Gstat, Gcritical, df['y'], max_index)
print(sorted(df['y']))

