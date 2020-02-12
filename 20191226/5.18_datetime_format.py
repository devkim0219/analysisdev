import pandas as pd

df = pd.read_csv('./data4/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
print(df.head())

df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())

# TimeStamp를 Period로 변환하여 년월일 표기 변경하기
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())

df.set_index('Date_m', inplace=True)
print(df.head())