import folium
import os
import json

#logoIcon = folium.features.CustomIcon('icon-hotel-png-3.png')
m = folium.Map(location=[28.207026, 83.985162],zoom_start=12)
tooltip='Click for more info'
'''folium.Marker(location=[28.207026,83985162],popup=<i>kaligandaki Hotel</i>,tooltip=tooltip).add_to(m)
folium.CircleMarker(location=[28.207026, 83.985162],
    radius=50,
    popup='Some Other Location',
    fill=True))'''
#overlay=os.path.join('data','overlay.json')
folium.Circle(location=[28.207026, 83.985162],
                    radius='5150',
                    popup="Welcome To Pokhara",
                    color='black',
                    fill=True,
                    fill_color='aquamarine'    
                    ).add_to(m)
folium.Marker(location=[28.213412,84.000380],
    popup='<strong>Hope guesthouse Nepal</strong>',
    icon=folium.Icon(color='green',icon='info-sign')).add_to(m)


folium.Marker(location=[28.213412,83.985162],
    popup='<strong>Kaligandaki</strong>',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(location=[28.215137,83.985643],
    popup='<strong>Hotel Deep Sagar Restaurant & Bar</strong>',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(location=[28.202243,83.9657894],
    popup='<strong>Hotel Mountain view</strong>',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)
folium.Marker(location=[28.203631,83.967345],
    popup='<strong>New Annapurna Guest House</strong>',
    icon=folium.Icon(color='green', icon='info-sign')
).add_to(m)

#folium.GeoJson(overlay,name='Pokhara').add_to(m)

m.save('main.html')