import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail())
print(type(df))

add = df + 10
# print(add.tail())
# print(type(add))

sub = add - df
print(sub.tail())
print(type(sub))