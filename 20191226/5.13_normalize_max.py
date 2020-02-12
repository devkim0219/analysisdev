import pandas as pd
import numpy as np

file_path = './data4/auto-mpg.csv'
df = pd.read_csv(file_path, header=None)
print(df.head())

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horsepower 열의 누락 데이터('?')를 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

print(df.horsepower.describe())

df.horsepower = df.horsepower / abs(df.horsepower.max())
print(df.horsepower.head())
print(df.horsepower.describe())