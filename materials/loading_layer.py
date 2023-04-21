project = QgsProject.instance()
raster_layer = QgsRasterLayer(
    'https://github.com/qgis/QGIS-Sample-Data/blob/master/'
    'qgis_sample_data/raster/SR_50M_alaska_nad.tif?raw=true',
    'alaska'
)
raster_layer.isValid()
project.addMapLayer(raster_layer)
