import json
import shapely
from shapely.geometry import shape
with open('/home/urpoadmin/pan.geojson') as json_data:
    jsn = json.load(json_data)
    geom = shape(jsn)

bowtie = Polygon(geom.coords)
bowtie.is_valid
clean = bowtie.buffer(0)
clean.is_valid
