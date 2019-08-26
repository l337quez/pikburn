#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http://www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http://www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
#############################################################################

from PySide import QtCore, QtGui


class TabDialog(QtGui.QDialog):
    def __init__(self, fileName, parent=None):
        super(TabDialog, self).__init__(parent)

        fileInfo = QtCore.QFileInfo(fileName)

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(GeneralTab(fileInfo), "General")
        tabWidget.addTab(PermissionsTab(fileInfo), "Config")
        tabWidget.addTab(ApplicationsTab(fileInfo), "Programmer")

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        # Titulo de la ventana
        self.setWindowTitle("PikBurn")
        # Icono en la ventana
        self.setWindowIcon(QtGui.QIcon('PikBurn4.png'))    


##REVISAR LOS BOXLAYOUT  http://zetcode.com/gui/pysidetutorial/layoutmanagement/



class GeneralTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(GeneralTab, self).__init__(parent)

        fileNameLabel = QtGui.QLabel("Chip Selector:")
        fileNameEdit = QtGui.QLineEdit(fileInfo.fileName())


        combo = QtGui.QComboBox(self)
        #movemos combo (x,y)
        combo.move(480, 280)

        combo.currentIndexChanged.connect(self._cb_currentIndexChanged)
        combo.highlighted.connect(self._cb_highlighted)

        items = ('', 'PIC16F83', 'PIC16F84', 'PIC16F84A', 'PIC16F87')
        combo.addItems(items)


        # Imiagen posicion del PIC en el ZIF
        label=QtGui.QLabel(self)
        label.setPixmap(QtGui.QPixmap("PIN18.png"))
        label.move(470, 0)
        
        
        # A vertical box layout 
        layout   =   QVBoxLayout ( ) 
        
        # Add the widgets to the layout 
        layout . addWidget ( fileNameLabel ) 
        layout . addWidget ( combo ) 
        layout . addWidget ( label ) 
        
        # Set layout as the layout for the window 
        win . setLayout ( layout ) 

       
        
        
        
        
#USAR UN FORMLAYOUT PARA PODER ACOMODAR T

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(fileNameLabel)
        mainLayout.addWidget(combo)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)
        
    # Funciones para concer la posicion selecionada del combo
    def _cb_currentIndexChanged(self, idx):
            print ('current selected index:', idx)

    def _cb_highlighted(self, idx):
            print ('highlighted index:', idx)





class PermissionsTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(PermissionsTab, self).__init__(parent)

        permissionsGroup = QtGui.QGroupBox("Permissions")

        readable = QtGui.QCheckBox("Readable")
        if fileInfo.isReadable():
            readable.setChecked(True)

        writable = QtGui.QCheckBox("Writable")
        if fileInfo.isWritable():
            writable.setChecked(True)

        executable = QtGui.QCheckBox("Executable")
        if fileInfo.isExecutable():
            executable.setChecked(True)

        ownerGroup = QtGui.QGroupBox("Ownership")

        ownerLabel = QtGui.QLabel("Owner")
        ownerValueLabel = QtGui.QLabel(fileInfo.owner())
        ownerValueLabel.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)

        groupLabel = QtGui.QLabel("Group")
        groupValueLabel = QtGui.QLabel(fileInfo.group())
        groupValueLabel.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Sunken)

        permissionsLayout = QtGui.QVBoxLayout()
        permissionsLayout.addWidget(readable)
        permissionsLayout.addWidget(writable)
        permissionsLayout.addWidget(executable)
        permissionsGroup.setLayout(permissionsLayout)

        ownerLayout = QtGui.QVBoxLayout()
        ownerLayout.addWidget(ownerLabel)
        ownerLayout.addWidget(ownerValueLabel)
        ownerLayout.addWidget(groupLabel)
        ownerLayout.addWidget(groupValueLabel)
        ownerGroup.setLayout(ownerLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(permissionsGroup)
        mainLayout.addWidget(ownerGroup)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


class ApplicationsTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(ApplicationsTab, self).__init__(parent)

        topLabel = QtGui.QLabel("Open with:")

        applicationsListBox = QtGui.QListWidget()
        applications = []

        for i in range(1, 31):
            applications.append("Application %d" % i)

        applicationsListBox.insertItems(0, applications)

        alwaysCheckBox = QtGui.QCheckBox()

        if fileInfo.suffix():
            alwaysCheckBox = QtGui.QCheckBox("Always use this application to "
                    "open files with the extension '%s'" % fileInfo.suffix())
        else:
            alwaysCheckBox = QtGui.QCheckBox("Always use this application to "
                    "open this type of file")

        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(applicationsListBox)
        layout.addWidget(alwaysCheckBox)
        self.setLayout(layout)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    if len(sys.argv) >= 2:
        fileName = sys.argv[1]
    else:
        fileName = "."


    
    tabdialog = TabDialog(fileName)
    # Tamaño de la ventana  (ancho,alto)
    tabdialog.resize(600,450)   
    sys.exit(tabdialog.exec_()) 














