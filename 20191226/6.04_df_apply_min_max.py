import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())

def min_max(x):
    return x.max() - x.min()

# dataframe 의 각 column 을 인수로 전달하면 series 를 반환
result = df.apply(min_max)
print(result)
print(type(result))