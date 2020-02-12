import seaborn as sns

df = sns.load_dataset('titanic')

# print(df.head())

nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)

# print(df.head().notnull())
# print(df.head().isnull())
print(df.head().isnull().sum(axis=0))