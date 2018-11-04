import folium
import pandas

low_elev = 1500
mid_elev = 3000
opacity = 0.8

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
    if elev < low_elev:
        return 'green'
    if low_elev <= elev < mid_elev:
        return 'orange'
    if elev >= mid_elev:
        return 'red'


map = folium.Map(location=[44, -120], zoom_start=6, tiles='Mapbox Bright')

fg = folium.FeatureGroup(name='My Map')

for name, elev, lat, lon in zip(name, elev, lat, lon):
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=html.format(
        name, str(elev)), fill=True, fill_opacity=opacity, fill_color=color_producer(elev), color='grey'))

map.add_child(fg)

map.save('webmap.html')
