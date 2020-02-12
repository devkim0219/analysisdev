import pandas as pd

file_path = './data2/남북한발전전력량.xlsx'

df1 = pd.read_excel(file_path)
print(df1)
print()

df2 = pd.read_excel(file_path, header=None)
print(df2)
print()