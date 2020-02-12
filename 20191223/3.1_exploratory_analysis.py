import pandas as pd

df = pd.read_csv('./data3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# print(df.head())
# print()
# print(df.tail())
# print()
# print(df.shape)
# print()
# print(df.info())
# print()
# print(df.dtypes)
# print()
# print(df.mpg.dtypes)
# print()
print(df.describe())
print()
print(df.describe(include='all'))