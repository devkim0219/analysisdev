import pandas as pd
import numpy as np

file_path = './data4/auto-mpg.csv'

df = pd.read_csv(file_path, header=None)

print(df.head())

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)

# print(df['horsepower'].dtypes)

# orgin 열의 문자열 자료형을 범주형으로 변환
df['origin'] = df['origin'].astype('category')
# print(df['origin'].dtypes)

# 범주형을 문자열로 다시 변환
df['origin'] = df['origin'].astype('str')
# print(df['origin'].dtypes)