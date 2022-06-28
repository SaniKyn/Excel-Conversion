import pandas as pd

k = float(input("Введите курс в рублей:"))
df = pd.DataFrame({'RusRub': [1000, 200123, 1234, 123]})
num = []
for i in df['RusRub']:
    n = round(i * k, 2)
    num.append(n)

df1 = pd.DataFrame({'BelRub': num})
salary_sheets = {'Group1': df, 'Group2': df1}
writer = pd.ExcelWriter('D:/python/ExcelPython/Сonversion.xlsx', engine='xlsxwriter')

for sheet_num in salary_sheets.keys():
    salary_sheets[sheet_num].to_excel(writer, sheet_name=sheet_num, index=False)

writer.save()