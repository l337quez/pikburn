from functools import partial
import sys
from PySide.QtCore import SIGNAL
from PySide.QtGui import QApplication, QLabel, QWidget
from PySide.QtGui import QPushButton, QVBoxLayout
from PySide2.QtGui import QIcon # Get the package to add an icon
 
########################################################################
class main(QWidget):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(main, self).__init__()
 
        layout = QVBoxLayout()
 
        self.label = QLabel("You haven't pressed a button!")
 
        # use a normal signal / slot mechanic
        button1 = QPushButton("One")
        self.connect(button1, SIGNAL("clicked()"), self.one)
 
        # now let's use partial functions
        button2 = QPushButton("Two")
        self.connect(button2, SIGNAL("clicked()"),
                     partial(self.onButton, "Two"))
 
        button3 = QPushButton("Three")
        self.btn3Callback = partial(self.onButton, "Three")
        button3.clicked.connect(self.btn3Callback)
 
        # now let's try using a lambda function
        button4 = QPushButton("Four")
        button4.clicked.connect(lambda name="Four": self.onButton(name))
        
        
        
         
        # Imiagen posicion del PIC en el ZIF
        #label=QLabel(self)
        #label.setPixmap(layout.QPixmap("PIN18.png"))
        #label.move(470, 0)
        
            
        #Icono en la ventana
        #icono=self.setWindowIcon(QIcon('PikBurn3.png')) 
        #QApplication.setWindowIcon('PikBurn3.png')
        #self.setWindowIcon(QIcon('PikBurn3.png'))   
        
        


        # boton conectar
        #self.bconect= QtGui.QPushButton("Conectar",self)
        #self.bconect.clicked.connect(self.port)
        #self.bconect.move(10, 10)        
        
        
        
        
        
 
        #layout.addWidget(icono)
        layout.addWidget(self.label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        self.setLayout(layout)
 
        #self.setWindowTitle("PySide Demo")
        
        

        
        
 
    #----------------------------------------------------------------------
    def one(self):
        """"""
        self.label.setText("You pressed One!")
 
    #----------------------------------------------------------------------
    def onButton(self, lbl):
        """Change the label to the text (lbl) passed in"""
        self.label.setText("You pressed %s!" % lbl)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication([])
    form = main()
    # Tamaño de la ventana
    form.resize(600,450)
    #NOmbre de la ventana
    form.setWindowTitle("PikBurn")

    
    form.show()
    app.exec_() 


