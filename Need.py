import pandas as pd
import xlsxwriter

df = pd.read_excel('my_m4.xlsx', sheet_name='Лист1')
workbook = xlsxwriter.Workbook('my_m4_new.xlsx')
worksheet = workbook.add_worksheet()

num = []
for i in df.iloc[:, 1]:
    list_str = i.split(' ')
    if list_str[0].upper():
        num.append(list_str[0].lower())


for i in range(len(num)):
    worksheet.write(f"A{i}", num[i])

workbook.close()
