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
        #movemos combo (x,y)
        combo.move(480, 292)

        combo.currentIndexChanged.connect(self._cb_currentIndexChanged)
        combo.highlighted.connect(self._cb_highlighted)

        #items = ('', 'PIC16F83', 'PIC16F84', 'PIC16F84A', 'PIC16F87')
        items = ('','PIC16F84A')
        combo.addItems(items)
        
        #label 
        label1 = QtGui.QLabel(self)
        label1.setText("Chip Selector:")
        label1.move(480, 271)
        
        # label autor y version
        lversion = QtGui.QLabel(self)
        lversion.setText("PikBurn V. Alpha 0.001     Developed by: Ronal Forero")
        lversion.move(0, 428)
        
        #label de la tarje
        lboard = QtGui.QLabel(self)
    

        
        #label del puerto
        #lboard = QtGui.QLabel(self)
        #lboard.setText("Chip Selector:")
        #lboard.move(30, 10)     
        
        # Imiagen posicion del PIC en el ZIF
        label=QtGui.QLabel(self)
        label.setPixmap(QtGui.QPixmap("PIN18.png"))
        label.move(470, 0)
        
            
        #Icono en la ventana
        self.setWindowIcon(QtGui.QIcon('PikBurn3.png'))    
        
        #label 
        #label1 = QtGui.QLabel(self)
        #label1.setText("Chip Selector:")
        #label1.move(480, 271)
        
        # label 
        self.label1= QtGui.QLabel("Chip Selector:")
        label1.move(480, 271)

        # boton conectar
        self.bconect= QtGui.QPushButton("Conectar",self)
        self.bconect.clicked.connect(self.port)
        self.bconect.move(10, 10)
        
        
        
       
        
# Funcion para conocer la posicion del combobox del selector de pic
    def _cb_currentIndexChanged(self, idx):
        print ('current selected index:', idx)

    def _cb_highlighted(self, idx):
        print ('highlighted index:', idx)
        


    #Funcion para conocer el puerto y el nombre de manufactura
    def port(self):
        #Aqui vemos la direccion /dev/tty****
        puerto=sorted( x[0] for x in comports() )
        print (puerto)
        puerto= ''.join(puerto)
        print (puerto)
        
        #limpiamos para que no hallan mensajes montadas
        puerto= puerto + "                               "
        print (puerto)
        #Buscamos la ide
        ruta_id=sorted( x[2] for x in comports() )
        #Convertimos de list a string
        ruta_id= ''.join(ruta_id)

        #Validamos si hay algo conectado
        status_conect=sorted( x[0] for x in comports() )
        if (status_conect == []):
            conexion= int(0)
            puerto= "Dispositivo desconectado"
            board= "                                                                                                  "
            name_board = Label(ventana, text =board).place(x=90, y=94)

        else:
            conexion= int(1)
            #Buscamos el numero ID del puerto
            id1=ruta_id.rindex(":")
            id2=id1 + 1
            id3= id1 + 5
            id_puerto=ruta_id[id2:id3]
            #Buscamos el nombre de la empresa manufacturera a partir del ID
            ruta_name_port= subprocess.check_output( "lsusb", stderr=subprocess.STDOUT, shell=True)
            #Convertimos de bytes a string
            ruta_de_port= ruta_name_port.decode("utf-8")
            #Buscamos el ID del puerto
            ruta_name_port1=ruta_de_port.index(id_puerto)
            ruta_name_port2=ruta_name_port1 + 4
            #Extraemos el nombre de manufactura
            name_port=ruta_de_port[ruta_name_port1:ruta_name_port2]
            ruta_name_port2=ruta_name_port1 + 5
            ruta_name_port3=ruta_name_port1 + 60
            name_board=ruta_de_port[ruta_name_port2:ruta_name_port3]
            #Buscamos el salto de linea que esta luego de la linea deseada
            name_board1=name_board.index("Bus")
            #Guardamos en board la posicion cero hasta antes de la palabra Bus
            board= name_board[0:name_board1] + "                                    "
            
            
            lboard.setText(board)
            lboard.move(0, 0)   
            #name_board = Label(ventana, text =board).place(x=50, y=94)


        #mensaje_puerto = Label(ventana, text =puerto).place(x=100, y=64)




      







    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)





    demo = Demo()
    # Tamaño de la ventana
    #demo.resize(ancho,alto)
    demo.resize(600,450)
    #NOmbre de la ventana
    demo.setWindowTitle("PikBurn")
    demo.show_and_raise()


    sys.exit(app.exec_())
