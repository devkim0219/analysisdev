import seaborn as sns

df = sns.load_dataset('titanic')

print(df.head())
print(df.info())

print(df['embark_town'][825:830])

# embark_town 열의 NaN 값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
# print(most_freq)

df['embark_town'].fillna(most_freq, inplace=True)
print(df['embark_town'][825:830])