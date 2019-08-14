#!/usr/bin/python
#Importamos las clases de PySide
import sys
from PySide import QtCore,QtGui


# #Creamos una aplicacion Qt
app = QtGui.QApplication(sys.argv)
mainwindow= QtGui.QWidget()
mainwindow.resize(400,350)
mainwindow.setWindowTitle("PikBurn")
mainwindow.show()

sys.exit(app.exec_())











#!/usr/bin/python

# Importamos las clases de PySide
# import sys
# from PySide.QtCore import *
# from PySide.QtGui import *

# #Creamos una aplicacion Qt
# app = QApplication(sys.argv)
# #Creamos una etiqueta y la mostramos
# label = QLabel("hola")
# label.show()
# app.exec_()
# sys.exit()
