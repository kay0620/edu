import folium

#Zoom 
#tiles : Stamen Toner, Stamen Terrain
#size : width, height
m = folium.Map(location = [35.1795543,129.0756416], 
               zoom_start = 13, 
               tiles="Stamen Toner",
               width = 750, height = 500
              )
m
