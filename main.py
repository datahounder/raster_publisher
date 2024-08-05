import gdal
gdal.UseExceptions()
rasin="D:\Users\www\Desktop\obrezka\imagery_ms.tif"
rasout="D:\Users\www\Desktop\obrezka\test.tif"
shpin="D:\Users\www\Desktop\pan.geojson"
try:
	result = gdal.Warp(rasout, rasin, cutlineDSName=shpin)
except RuntimeError as err:
	print('Handlingf run - time error:', err)
	print('kori1')
print('kori2')
