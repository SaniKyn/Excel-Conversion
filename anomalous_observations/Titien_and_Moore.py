import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_excel('test.xlsx', sheet_name='Лист1')


def truncated_data(y):
    k = []
    avg_y = np.mean(y)
    abs_val_minus_avg = abs(y - avg_y)
    for i in abs_val_minus_avg:
        if avg_y < i:
            k.append(abs_val_minus_avg)
    max_ind = np.argmax(abs_val_minus_avg)
    norm_values = sorted(y)[:-len(k)]
    average_value_common_k = np.sum(norm_values) / (len(y) - len(k))
    return average_value_common_k, norm_values, max_ind


def titien_and_moore(average, n, df):
    sum_n = np.sum((n - average) ** 2)
    sum_df = np.sum((df - average) ** 2)
    e = round(sum_n / sum_df, 2)
    print('Критерий грубых ошибок в данных, расположенных в нижней части ранжированного ряда данных', e)
    return e


def result_tm(e):
    if e < 0.221:
        print('Все ошибки грубые')


avck, norm, max_i = truncated_data(df['y'])
eh = titien_and_moore(avck, norm, df['y'])
result_tm(eh)
