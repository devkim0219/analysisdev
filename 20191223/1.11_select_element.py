import pandas as pd

exam_data = {'이름': ['서준', '우현', '인아'], '수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
print(df)
print(type(df))
print()

a = df.loc['서준', '음악']
# print(a)
# print()

b = df.iloc[0, 2]
# print(b)
# print()

c = df.loc['서준', ['음악', '체육']]
# print(c)
# print()

d = df.iloc[0, [2, 3]]
# print(d)
# print()

e = df.loc['서준', '음악':'체육']
# print(e)
# print()

f = df.iloc[0, 2:]
# print(f)
# print()

g = df.loc[['서준', '우현'], ['음악', '체육']]
# print(g)
# print()

h = df.iloc[[0, 1], [2, 3]]
# print(h)
# print()

i = df.loc['서준':'우현', '음악':'체육']
# print(i)
# print()

j = df.iloc[0:2, 2:]
# print(j)
# print()

df.loc['서준', '음악'] = 90
print(df)