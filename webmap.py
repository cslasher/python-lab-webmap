import folium
import pandas

volcanoes = pandas.read_csv('Volcanoes.csv')
lat = list(volcanoes.LAT)
lon = list(volcanoes.LON)
name = list(volcanoes.NAME)
elev = list(volcanoes.ELEV)

html = '''
<a href="https://www.google.com/search?q=%22{0}%22" target="_blank">{0}</a><br>
Height: {1} m
'''


def color_producer(elev):
    if elev < 1500:
        return 'green'
    if 1500 <= elev < 3000:
        return 'orange'
    if elev >= 3000:
        return 'red'


map = folium.Map(location=[44, -120], zoom_start=6, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')

for name, elev, lat, lon in zip(name, elev, lat, lon):
    fg.add_child(folium.Marker(location=[lat, lon], popup=html.format(
        name, str(elev)), icon=(folium.Icon(color=color_producer(elev)))))

map.add_child(fg)

map.save('webmap.html')
