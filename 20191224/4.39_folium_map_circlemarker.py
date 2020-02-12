import folium
import pandas as pd

df = pd.read_excel('./data4/서울지역 대학교 위치.xlsx')

seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)

for name, lat, lng in zip(df.iloc[:, 0], df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=10,
                        color='brown',
                        fill=True,
                        fill_color='coral',
                        fill_opacity=0.7,
                        popup=name
    ).add_to(seoul_map)

# seoul_map.save('./output/seoul_colleges2.html')