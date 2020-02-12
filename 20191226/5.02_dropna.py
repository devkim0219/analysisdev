import seaborn as sns

df = sns.load_dataset('titanic')

print(df.head())

missing_df = df.isnull()

for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()

    # try:
    #     print(col, ': ', missing_count[True])
    # except:
    #     print(col, ': ', 0)

# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
df_thresh = df.dropna(axis=1, thresh=500)
# print(df_thresh.columns)

# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
df_age = df.dropna(subset=['age'], how='any', axis=0)
# print(len(df_age))

df_1 = df

for col in df.columns:
    df_1[col] = df.dropna(subset=[col], how='any', axis=0)
    # df_1 = df.dropna(subset=[col], how='any', axis=0)

print(df_1.head())