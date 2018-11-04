import folium
import pandas

low_elev = 1500
mid_elev = 3000
opacity = 0.8
pop_tier_one = 10000000
pop_tier_two = 20000000


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

fgp = folium.FeatureGroup(name='Populations')

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda
                             x: {'fillColor': 'green' if x['properties']['POP2005'] < pop_tier_one
                                 else 'orange' if x['properties']['POP2005'] < pop_tier_two
                                 else 'red'}))

fgv = folium.FeatureGroup(name='Vocanoes')

for name, elev, lat, lon in zip(name, elev, lat, lon):
    fgv.add_child(folium.CircleMarker(location=[lat, lon], popup=html.format(
        name, str(elev)), fill=True, fill_opacity=opacity, fill_color=color_producer(elev), color='grey'))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save('webmap.html')
