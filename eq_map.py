import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = 'data/eq_data_30_day_m1.json'
with open(data) as f:
    eq_data = json.load(f)

eq_dicts = eq_data['features']
mags, lons, lats, text = [], [], [], []
for eq_dict in eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    text.append(title)

# Earthquakes map
earth_map = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

layout = Layout(title='Earthquakes map')

fig = {'data':earth_map, 'layout': layout}
offline.plot(fig, filename='earthquakes.html')
