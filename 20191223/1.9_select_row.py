import pandas as pd

exam_data = {'수학': [90, 80, 70], '영어': [98, 89, 95], '음악': [85, 95, 100], '체육': [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print()

label_1= df.loc['서준']
position1 = df.iloc[0]
# print(label_1)
# print()
# print(position1)

label_2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0, 1]]
print(label_2)
print()
print(position2)