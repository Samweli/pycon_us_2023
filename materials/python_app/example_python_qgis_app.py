from qgis.core import *
from qgis.gui import QgsMapCanvas
from qgis.PyQt.QtWidgets import QFrame, QGridLayout, QMainWindow

application = QgsApplication([], False)

# The prefix path varies depending on the method of installation
# used to install QGIS and the OS in use.
# If conda package manager was used to install QGIS then the
# prefix path should be location of the qgis package.
# Otherwise the prefix path should be the location of where
# QGIS application has been installed.
QgsApplication.setPrefixPath('/usr', True)
QgsApplication.initQgis()

main_window = QMainWindow()
main_window.setWindowTitle(
    "Python with QGIS example | "
    "PyCon US 2023"
)
frame = QFrame()
main_window.setCentralWidget(frame)
layout = QGridLayout(frame)

map_canvas = QgsMapCanvas()
layout.addWidget(map_canvas)

raster_file_uri = 'https://github.com/qgis/QGIS-Sample-Data/' \
                  'blob/master/qgis_sample_data/raster/' \
                  'SR_50M_alaska_nad.tif?raw=true'

open_street_map_uri = 'type=xyz&url=https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&' \
                      'zmax=19&zmin=0&http-header:referer='

raster_layer = QgsRasterLayer(raster_file_uri, 'test_layer')

QgsProject.instance().addMapLayer(raster_layer)
map_canvas.setLayers([raster_layer])
map_canvas.setExtent(raster_layer.extent())

main_window.show()
application.exec_()
