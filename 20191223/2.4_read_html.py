import pandas as pd

url = './data2/sample.html'

tables = pd.read_html(url)
# print(len(tables))

# for i in range(len(tables)):
#     print('tables[%s]' % i)
#     print(tables[i])
#     print()

df = tables[1]
print(df)