import requests
import json

r = requests.get('https://raw.githubusercontent.com/kay0620/edu/main/folium/busan_gu.json')
                
c = r.content                 
                 
# 지역 좌표 추출
busan_geo = json.loads(c)


import folium
#지도 띄우기
m = folium.Map(location = [35.1795543,129.0756416],
               zoom_start = 11,
               tiles='cartodbpositron')


#경계값
folium.GeoJson(busan_geo,name = '지역구').add_to(m)

m
