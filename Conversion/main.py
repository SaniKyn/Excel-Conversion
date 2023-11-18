import pandas as pd

k = float(input("Введите курс в рублей:"))
df = pd.read_excel('Сonversion.xlsx', sheet_name='Sheet1')
num = []
for i in df['RusRub']:
    n = round(i * k, 2)
    num.append(n)

df['bel'] = num
df.to_excel('D:/Works/Excel-Conversion/Сonversion.xlsx', index=False)
