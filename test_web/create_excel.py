# _*_ coding:utf-8 _*_
import pandas as pd
a = ['a','b','c']
b = [1,2,3]
dit = {'char':a, 'num':b}
file_path = r'./output.xlsx'
writer = pd.ExcelWriter(file_path)
df = pd.DataFrame(dit)
#columns参数用于指定生成的excel中列的顺序
df.to_excel(writer, columns=['char','num'], index=False,encoding='utf-8',sheet_name='Sheet')
writer.save()