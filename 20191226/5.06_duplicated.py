import pandas as pd

df = pd.DataFrame({'c1': ['a', 'a', 'b', 'a', 'b'],
                   'c2': [1, 1, 1, 2, 2],
                   'c3': [1, 1, 2, 2, 2]})

df_dup = df.duplicated()
# print(df_dup)

col_dup = df['c2'].duplicated()
print(col_dup)

col_not_dup = df[col_dup != True]
print(col_not_dup)