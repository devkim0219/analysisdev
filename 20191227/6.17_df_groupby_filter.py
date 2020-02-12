import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head(), '\n')
print(type(grouped_filter), '\n')

age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter.head(), '\n')
print(type(age_filter), '\n')