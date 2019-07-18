"""
using: Leaflet
File.csv
"""

import folium
import pandas as pd

data = pd.read_csv('File.csv') #Importing file
fg = folium.FeatureGroup(name='Basic Map')

lat, lon, elev, name = list(data['LAT']), list(data['LON']), list(data['ELEV']), 'Volcano'

#Color return for map circles
def icon_color(elev) -> str:
    if elev <= 2000: return 'green'
    elif elev <= 3000 and elev > 2000: return 'orange'
    elif elev > 3000: return 'red'


#Styling and html for popup
event_html = """
<style type="text/css" media="screen"> .styler{text-align: center; text-decoration: none; color:#5b4f4f; font-size: 20px; font-family: Calibri;} .styler a{text-decoration: none; color: #9d2727} .styler a:hover{text-decoration: none; color: 9d9a9a;} </style> <div class="styler"> <h4><a href="https://upload.wikimedia.org/wikipedia/commons/9/93/Lava_fountain_USGS_page_30424305-068_large.JPG" target="_blank">%s</a> Elevation: <i>%s m</i></h4> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Lava_fountain_USGS_page_30424305-068_large.JPG/330px-Lava_fountain_USGS_page_30424305-068_large.JPG" /> <br><br> </div>
"""

map = folium.Map(location=[40.6799011,-121.5510025], zoom_start=6)#, #tiles='https://{s}.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png?apikey=65dc0091429442be8ed1e7deac57bf41', attr='<a href=http://www.thunderforest.com/>Thunderforest</a>, &copy; <a href=https://www.openstreetmap.org/copyright>'
    #https://leaflet-extras.github.io/leaflet-providers/preview/, #tiles='https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png', attr="<a href=https://endless-sky.github.io/>Endless Sky</a>"#,
    #max_zoom=18

for lt, ln, ele in zip(lat, lon, elev):
    frame = folium.IFrame(html=event_html %(name, ele), width=400, height=325)
    fg.add_child(folium.CircleMarker(location=(lt, ln), radius=8, popup=folium.Popup(frame), fill_color = icon_color(ele), fill_opacity = 0.7, fill = 'grey', line_color = 'black' ))

map.add_child(fg)
map.save('map-basic-features.html') #Save the file name.
