import geopandas as gp
faultyshapefile = gp.read_file('/home/urpoadmin/pan.geojson')
nonecontroller = 0
while nonecontroller == 0:
    nonecontroller = 1
    for i in range(len(faultyshapefile)):
        shape=faultyshapefile.iloc[i]['geometry']
        print(shape)
        if shape.is_valid != True:
            faultyshapefile = faultyshapefile.drop([i], axis=0)
            print(faultyshapefile.drop([i], axis=0))
            nonecontroller = 0
            break