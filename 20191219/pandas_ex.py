import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv('./data/gapminder.tsv', sep='\t')

# print(df.head(20))
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

# country_df = df['country']
# print(country_df)

# 마지막 행 데이터 가져오기
# number_of_rows = df.shape[0]
# last_row_index = number_of_rows - 1
# print(df.loc[last_row_index])

# print(df.loc[[0, 99, 999]])
# print(df.iloc[[0, 99, 999]])
# print(df.loc[:, ['year', 'pop']])
# print(df.iloc[:, [2, 4, -1]])

# a = df.groupby(['year', 'continent'])['lifeExp', 'gdpPercap'].mean()

# print(a)
# print('########')
# print(a.iloc[-1])

# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'

# df_data = pd.read_csv(data_url, sep='\s+', header = None)

# df_data.head()
# df_data.tail()

# scientists = pd.DataFrame(
#     data={'Occupation' : ['Chemists', 'Statistician'],
#           'Born' : ['1920-07-25', '1876-06-13'],
#           'Died' : ['1958-04-16', '1937-10-16'],
#           'Age' : [37, 61]},
#     index=['Rosaline Franklin', 'William Gosset'],
#     columns=['Occupation', 'Born', 'Died', 'Age'])

# first_row = scientists.loc['William Gosset']

# # print(first_row)
# print(first_row.index)
# print(first_row.values)

# sentence = 'Life is too short, you need python'

# def delete_moeum(sentence):
#     moeum = 'aiueo'
#     # charList = [char for char in sentence if char not in moeum]
#     charList = []

#     for char in sentence:
#         if char not in moeum:
#             charList.append(char)

#     return charList

# result = delete_moeum(sentence)
# print(''.join(result))

# scientists = pd.read_csv('./data/scientists.csv')
# print(scientists)

# ages = scientists['Age']
# print(ages)

# print(ages > ages.mean())

# def over_ages(ages):
#     overAgeList = []

#     for age in ages:
#         if age > ages.mean():
#             overAgeList.append(age)

#     return overAgeList

# print(over_ages(ages))

# ages.to_pickle('./output/ages.pickle')

# ages = pd.read_pickle('./output/ages.pickle')
# print(ages)

anscombe = sns.load_dataset('anscombe')

print(anscombe)
print(type(anscombe))

dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

result = plt.plot(dataset_1['x'], dataset_1['y'])

fig = plt.figure()
axes1 = fig.add_subplot(2, 2, 1)
axes2 = fig.add_subplot(2, 2, 2)
axes3 = fig.add_subplot(2, 2, 3)
axes4 = fig.add_subplot(2, 2, 4)

axes1.set_title('dataset_1')
axes2.set_title('dataset_2')
axes3.set_title('dataset_3')
axes4.set_title('dataset_4')

fig.show()