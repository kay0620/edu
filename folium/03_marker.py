import folium

m = folium.Map(location = [35.195959,129.0756416], zoom_start = 13)


htext = '<pre>KPC 서부산</pre>' 
folium.Marker([35.195959,129.081479],
             popup = htext, #'KPC 서부산',
             tooltip = 'Click me!',
             icon=folium.Icon(icon="cloud",color = 'red')).add_to(m)

#원형마커
folium.CircleMarker([35.195959,129.081479],
                    popup = htext,#'KPC 서부산',
                    tooltip = 'Click me!',
                    radius=50,
                    color="#3186cc",
                    fill=True,
                    fill_color="#3186cc").add_to(m)

m
