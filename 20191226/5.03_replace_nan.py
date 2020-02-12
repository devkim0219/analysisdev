import seaborn as sns

df = sns.load_dataset('titanic')

print(df.head())
print(df.info())

mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)

print(df['age'].head(10))