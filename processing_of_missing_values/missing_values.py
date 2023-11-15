import pandas as pd
import numpy as np
import random

df = pd.read_excel('...', sheet_name='Лист1')


# Randbetween
def randbetween(df):
    for i in df[['X1', 'X2', 'X3', 'X4']]:
        df[i] = df[i].apply(lambda x: round(random.uniform(df[i].min(), df[i].max()), 1) if np.isnan(x) else x)
    df.to_excel('...', index=False)


# Sample Averages
def sample_averages(df):
    for i in df[['X1', 'X2', 'X3', 'X4']]:
        x_i = round(df[i].sum() / df['Y'].count(), 1)
        df[i] = df[i].fillna(x_i)
    df.to_excel('...', index=False)


# bfill - след, ffill-передыдущие
def previous_and_next_values(df):
    for i in df[['X1', 'X2', 'X3', 'X4']]:
        df[i] = df[i].bfill().ffill()
    df.to_excel('...', index=False)


randbetween(df)
sample_averages(df)
previous_and_next_values(df)
