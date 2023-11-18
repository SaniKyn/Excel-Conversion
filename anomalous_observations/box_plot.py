import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('test.xlsx', sheet_name='Лист1')
df['y'].plot(kind='box')
plt.show()
