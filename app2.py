"""
File.csv
world.json
worldcities.csv
"""

import pandas as pd
import folium

data = pd.read_csv('File.csv')
cit_dat = pd.read_csv('worldcities.csv')

#Feature Groups
fg = folium.FeatureGroup(name='US Volacanos')
fgd = folium.FeatureGroup(name="World Population - 3 Layer")
fcl = folium.FeatureGroup(name='All World Cities')

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

map = folium.Map(location=[23.7221, 15.9347], zoom_start=2)#, #tiles='https://{s}.tile.thunderforest.com/spinal-map/{z}/{x}/{y}.png?apikey=65dc0091429442be8ed1e7deac57bf41', attr='<a href=http://www.thunderforest.com/>Thunderforest</a>, &copy; <a href=https://www.openstreetmap.org/copyright>'
    #https://leaflet-extras.github.io/leaflet-providers/preview/, #tiles='https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png', attr="<a href=https://endless-sky.github.io/>Endless Sky</a>"#,
    #max_zoom=18

for lt, ln, ele in zip(lat, lon, elev):
    frame = folium.IFrame(html=event_html %(name, ele), width=400, height=325)
    fg.add_child(folium.CircleMarker(location=(lt, ln), radius=8, popup=folium.Popup(frame), fill_color = icon_color(ele), fill_opacity = 0.7, fill = 'grey', line_color = 'black' ))

fgd.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

cit_dated= cit_dat[15:20] #City sliced
cit_lan, cit_lon = list(cit_dated['lat']), list(cit_dated['lng'])

for lat, lng in zip(cit_lan, cit_lon):
    fcl.add_child(folium.Marker(location=(lat, lng), icon = folium.Icon(color='green')))

map.add_child(fg)
map.add_child(fgd)
map.add_child(fcl)
map.add_child(folium.LayerControl())

map.save('3lyr-map-advance-features.html') #Save the file name.