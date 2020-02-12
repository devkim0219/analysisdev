import pandas as pd

file_path = './data4/auto-mpg.csv'

df = pd.read_csv(file_path, encoding='utf-8')

print(df.head())

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# mpg(mile per gallon)를 kpl(killometer per liter)로 변환(mpg_to_kpl = 0.425)
mpg_to_kpl = 1.60934 / 3.78541

df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head())