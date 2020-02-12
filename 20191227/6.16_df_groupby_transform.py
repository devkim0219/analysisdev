import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])

age_mean = grouped.age.mean()
print(age_mean, '\n')

age_std = grouped.age.std()
print(age_std, '\n')

for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin: ', key)
    print(group_zscore.head(3), '\n')

def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]], '\n')
print(len(age_zscore), '\n')
print(type(age_zscore))