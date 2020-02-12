import pandas as pd

df = pd.read_csv('./data3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# print(df.mean())
# print(df['mpg'].mean())
# print(df.mpg.mean())
# print(df[['mpg', 'weight']].mean())
# print()

# print(df.median())
# print(df['mpg'].median())
# print()

# print(df.max())
# print(df['mpg'].max())
# print()

# print(df.min())
# print(df['mpg'].min())
# print()

# 표준편차
# print(df.std())
# print(df['mpg'].std())
# print()

# 상관계수
print(df.corr())
print(df[['mpg', 'weight']].corr())
print()