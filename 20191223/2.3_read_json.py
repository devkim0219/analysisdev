import pandas as pd

file_path = './data2/read_json_sample.json'

df1 = pd.read_json(file_path)
print(df1)
print()
print(df1.index)