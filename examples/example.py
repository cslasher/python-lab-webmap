import folium
import pandas

volcanoes = pandas.read_csv('./examples/Volcanoes.csv')
lat = list(volcanoes.LAT)
lon = list(volcanoes.LON)
name = list(volcanoes.NAME)
elev = list(volcanoes.ELEV)

html = '''
<a href="https://www.google.com/search?q=%22{0}%22" target="_blank">{0}</a><br>
Height: {1} m
'''

map = folium.Map(location=[44, -120],
                 zoom_start=6, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')

for name, elev, lat, lon in zip(name, elev, lat, lon):
    fg.add_child(folium.Marker(location=[lat, lon], popup=html.format(
        name, str(elev)), icon=(folium.Icon(color='blue'))))

# for index, vol in volcanoes.iterrows():
#     fg.add_child(folium.Marker(location=[vol.LAT, vol.LON],
#                                popup='Here ' + str(index) + '!', icon=(folium.Icon(color='blue'))))

map.add_child(fg)

map.save('example.html')
