import folium
import pandas as pd

def color_producer(elevation):
    if elevation <3000:
        return 'green'
    elif  3000<=elevation < 4000:
        return 'orange'
    else:
        return 'red' 

    
volcanos_df = pd.read_csv("volcanes-mexico-txt.txt",sep=",")
map = folium.Map(location=[23.879030926816302, -102.18218324835266], tiles="OpenStreetMap")
fgv = folium.FeatureGroup(name='Volcanoes')


# for lat,lon,elev,name in zip(volcanos_df.LAT,volcanos_df.LON,volcanos_df.ELEV, volcanos_df.NAME):
#     fg.add_child(folium.Marker(location=(lat,lon), popup=name+'\n'+'Elevation:' +str(elev)+'m', icon=folium.Icon(color=color_producer(elev))))
for lat,lon,elev,name in zip(volcanos_df.LAT,volcanos_df.LON,volcanos_df.ELEV, volcanos_df.NAME):
    fgv.add_child(folium.CircleMarker(location=(lat,lon), popup=name+'\n'+'Elevation:' +str(elev)+'m',color=color_producer(elev),
                                     fill=True, fillOpacity=0.6, fillColor=color_producer(elev)))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 
                                                     else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                     else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map.html')

