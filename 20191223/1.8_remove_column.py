import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
# print(df)

df1 = df[:]
df1.drop('수학', axis=1, inplace=True)
# print(df1)

df2 = df[:]
df2.drop(['영어', '음악'], axis=1, inplace=True)
print(df2)