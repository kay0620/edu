import pandas as pd

df = pd.read_csv('부산광역시_금정구_무인단속카메라 설치 현황_20210913.csv'
                 , encoding='cp949'
                 #, usecols = ['설치장소','지번주소']
                )


# df.rename(columns = {' 위도 ':'위도',' 경도 ':'경도'},inplace=True)

new_index = []
for t in df.columns:
    new_index.append(t.replace(' ',''))

df.columns = new_index


import folium

m = folium.Map(
    location=[35.1795543,129.0756416],
    zoom_start=15
)

#데이터의 첫번째 값으로 위도 경도 설정
m = folium.Map(
    location=[df['위도'].iloc[0], df['경도'].iloc[0]],
    zoom_start=15
)

#마커 클러스터 확인
from folium.plugins import MarkerCluster
marker_cluster = MarkerCluster().add_to(m)

for lat, lng, name in zip(df['위도'], df['경도'], df['설치장소']):
    folium.Marker([lat,lng], icon = folium.Icon(icon='camera',color='green'),
                  popup = f'<pre>{name}</pre>').add_to(marker_cluster)
m
