import pandas as pd

url = './data2/sample.html'

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ['A', 'A+', 'B'],
        'basic': ['C', 'B', 'B+'],
        'c++': ['B+', 'C', 'C+']}

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

# df.to_csv('./output/df_sample_2.7.csv')