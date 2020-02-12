import pandas as pd

df = pd.DataFrame({'c1': ['a', 'a', 'b', 'a', 'b'],
                   'c2': [1, 1, 1, 2, 2],
                   'c3': [1, 1, 2, 2, 2]})

df_dup = df.duplicated()
# print(df_dup)

df2 = df.drop_duplicates()
print(df2)

df3 = df.drop_duplicates(subset=['c2', 'c3'])
print(df3)