import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

pd.set_option('display.max_columns', 10)

# 함께 탑승한 형제 또는 배우자의 수가 3, 4, 5인 승객만 따로 추출 - boolean indexing
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5

df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head(), '\n')

# isin() 메서드를 활용하여 동일한 조건으로 추출
isin_filter = titanic['sibsp'].isin([3, 4, 5])
df_isin = titanic[isin_filter]
print(df_isin.head(), '\n')