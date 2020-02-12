import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)

titanic = sns.load_dataset('titanic')

df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head(), '\n')

pdf1 = pd.pivot_table(df,               # 피벗할 데이터 프레임
                      index='class',    # 행 위치에 들어갈 열
                      columns='sex',    # 열 위치에 들어갈 열
                      values='age',     # 데이터로 사용할 열
                      aggfunc='mean')   # 데이터 집계 함수

print(pdf1.head(), '\n')

pdf2 = pd.pivot_table(df,
                      index='class',
                      columns='sex',
                      values='survived',
                      aggfunc=['mean', 'sum'])

print(pdf2.head(), '\n')

pdf3 = pd.pivot_table(df,
                      index=['class', 'sex'],
                      columns='survived',
                      values=['age', 'fare'],
                      aggfunc=['mean', 'max'])

print(pdf3.head(), '\n')

pd.set_option('display.max_columns', 10)
print(pdf3.head(), '\n')

# xs 인덱서 사용 - 행 선택(default: axis=0)
print(pdf3.xs('First'), '\n')               # 행 인덱스가 First 인 행을 선택
print(pdf3.xs(('First', 'female')), '\n')   # 행 인덱스가 ('First', 'female')인 행을 선택
print(pdf3.xs('male', level='sex'), '\n')         # 행 인덱스의 sex 레벨이 male 인 행을 선택
print(pdf3.xs(('Second', 'male'), level=[0, 'sex']), '\n')  # Second, male 인 행을 선택

# xs 인덱서 사용 - 열 선택(axis=1 설정))
print(pdf3.xs('mean', axis=1))              # 열 인덱스가 mean 인 데이터를 선택
print(pdf3.xs(('mean', 'age'), axis=1))     # 열 인덱스가 ('mean', 'age')인 데이터 선택
print(pdf3.xs(1, level='survived', axis=1)) # survived 레벨이 1인 데이터 선택