import requests
import pandas as pd
import folium
import csv

file_path = './data4/university_list_2019.xlsx'

df = pd.read_excel(file_path)

print(df)

df_1 = df[(df['연도'] == 2019) & (df['시도'] == '부산')].loc[:, ['학교명', '주소']]

print(df_1.head())

# KAKAO_API_KEY = 'bceac8fa829e15e03abd026e688b94c1'

# url = 'https://dapi.kakao.com/v2/local'.format('경남정보대학교')

# headers = {
#     'Authorization':'KakaoAK {0}'.format(KAKAO_API_KEY)
# }

# res = requests.get(url, headers=headers)
# res = res.json()

# print(res['documents'][0]['address_name'],
#       res['documents'][0]['y'],
#       res['documents'][0]['x'])