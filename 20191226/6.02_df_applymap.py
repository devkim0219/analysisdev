import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())

# 사용자 정의 함수
def add_10(n):
    return n + 10

# dataframe 에 applymap() 으로 add_10() 함수를 매핑 적용
df_map = df.applymap(add_10)
print(df_map.head())