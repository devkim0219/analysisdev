import pandas as pd

df = pd.read_csv('./data4/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
df.drop('Date', axis=1, inplace=True)
# print(df.head())

df.set_index('new_Date', inplace=True)
print(df.head())

df_y = df['2018']
print(df_y.head())

df_ym = df.loc['2018-07']
print(df_ym)

df_ym_cols = df.loc['2018-07', 'Start':'High']
print(df_ym_cols)

df_ymd = df['2018-07-02']
print(df_ymd)

df_ymd_range = df['2018-06-25':'2018-06-20']
print(df_ymd_range)

# 시간 간격 계산, 최근 180일 ~ 189일 사이의 값들만 선택하기
today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
df.set_index('time_delta', inplace=True)
df_180 = df['180 days':'189 days']
print(df_180)