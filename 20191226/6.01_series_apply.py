import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())

# 사용자 정의 함수
def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b

# print(add_10(10))
# print(add_two_obj(10, 10))

sr1 = df['age'].apply(add_10)
print(sr1.head())

sr2 = df['age'].apply(add_two_obj, b=10)
print(sr2.head())

# 람다 함수 활용: 시리즈 객체에 적용
sr3 = df['age'].apply(lambda x: x + 10)
print(sr3.head())