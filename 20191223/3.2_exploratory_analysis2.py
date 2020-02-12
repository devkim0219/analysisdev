import pandas as pd

df = pd.read_csv('./data3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print(df.count())
print(type(df.count()))
print()

unique_values = df['origin'].value_counts()
print(unique_values)
print(type(unique_values))