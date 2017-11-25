import folium
import pandas

dat=pandas.read_csv("Volcanoes_USA.txt")
lts=list(dat["LAT"])
lns=list(dat["LON"])
elv=list(dat["ELEV"])

def color_changer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map= folium.Map(location=[38.59, -99.09], zoom_start=6, tiles= 'Mapbox Bright')

vol= folium.FeatureGroup(name="Volcanoes_USA")
pop= folium.FeatureGroup(name="Population")

for lat,lon,el in zip(lts,lns,elv):
    vol.add_child(folium.CircleMarker(location=[lat,lon], popup=str(el)+"m",radius=10,fill=True,
     fill_color=color_changer(el), fill_opacity=0.7))

pop.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(vol)
map.add_child(pop)
map.add_child(folium.LayerControl())
map.save("area.html")
