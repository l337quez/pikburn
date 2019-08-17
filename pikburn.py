#!/usr/bin/python
#Importamos las clases de PySide

#revisar https://github.com/shuge/Qt-Python-Binding-Examples/tree/master/common_widgets

import sys
try:
    from PySide import QtCore
    from PySide import QtGui
except ImportError:
    from PyQt4 import QtCore
    from PyQt4 import QtGui




class Demo(QtGui.QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)


        combo = QtGui.QComboBox(self)
        combo.move(20, 20)

        combo.currentIndexChanged.connect(self._cb_currentIndexChanged)
        combo.highlighted.connect(self._cb_highlighted)

        items = ('', 'Lisp', 'C', 'Objective-C', 'Python', 'Java')
        combo.addItems(items)

    def _cb_currentIndexChanged(self, idx):
        print ('current selected index:', idx)

    def _cb_highlighted(self, idx):
        print ('highlighted index:', idx)

    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)




    demo = Demo()
    # Tamaño de la ventana
    demo.resize(400,350)
    #NOmbre de la ventana
    demo.setWindowTitle("PikBurn")
    demo.show_and_raise()


    sys.exit(app.exec_())
