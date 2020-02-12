import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print()

math = df['수학']
# print(math)
# print(type(math))
# print()

eng = df.영어
# print(eng)
# print(type(eng))
# print()

music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))