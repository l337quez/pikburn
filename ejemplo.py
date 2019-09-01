from functools import partial
from PySide.QtCore import SIGNAL
from PySide.QtGui import QApplication, QLabel, QWidget
from PySide.QtGui import QPushButton, QVBoxLayout
 
########################################################################
class MultiButtonDemo(QWidget):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(MultiButtonDemo, self).__init__()
 
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
 
        layout.addWidget(self.label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        self.setLayout(layout)
 
        self.setWindowTitle("PySide Demo")
 
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
    form = MultiButtonDemo()
    form.show()
    app.exec_() 
