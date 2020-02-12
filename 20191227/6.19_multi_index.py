import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')

df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class', 'sex'])

gdf = grouped.mean()
print(gdf, '\n')
print(type(gdf), '\n')

# class 값이 First 인 행을 선택하여 출력
print(gdf.loc['First'], '\n')

# class 값이 First 이고, sex 값이 female 인 행을 선택하여 출력
print(gdf.loc['First', 'female'], '\n')

# sex 값이 male 인 행을 선택하여 출력
print(gdf.xs('male', level='sex'), '\n')
print(gdf.xs('male', level=1, axis=0), '\n')