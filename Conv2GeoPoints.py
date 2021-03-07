import csv
import json
from collections import OrderedDict

li = []
with open('chips2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for cityId, place,population,lat,lon in reader:
        d = OrderedDict()
        d['type'] = 'Feature'
        d['geometry'] = {
            'type': 'Point',
            'coordinates': [float(lat), float(lon)]
        }
        d['properties'] = {
            'population': population,
            'place': place
        }
        li.append(d)

d = OrderedDict()
d['type'] = 'FeatureCollection'
d['features'] = li
with open('LocnPoints.json', 'w') as f:
    f.write(json.dumps(d, sort_keys=False, indent=4))
