import pandas as pd
import numpy as np

file_path = './data4/stock-data.csv'
df = pd.read_csv(file_path)
# print(df.head())
# print(df.info())

df['new_Date'] = pd.to_datetime(df['Date'])

# print(df.head())
# print()
# print(df.info())
# print()
# print(type(df['new_Date'][0]))

# 시계열 값으로 변환된 열을 새로운 행 인덱스로 지정. 기존 날짜 열은 삭제
df.set_index('new_Date', inplace=True)
df.drop('Date', axis=1, inplace=True)
print(df.head())
print()
print(df.info())