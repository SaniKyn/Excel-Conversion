import pandas as pd

k = float(input("Введите курс в рублей:"))
df = pd.read_excel('Сonversion.xlsx', sheet_name='Sheet1')
num = []
for i in df['RusRub']:
    n = round(i * k, 2)
    num.append(n)

df['BelRub'] = num
df.to_excel('D:/python/ExcelPython/Сonversion.xlsx', index=False)
