#!/usr/bin/python

import sys, os
from serial.tools.list_ports import comports
import subprocess

from PySide6 import QtCore, QtGui, QtWidgets
from about_tab import AboutTab
from number_text_area import QCodeEditor


class Demo(QtWidgets.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        
        #layout = QVBoxLayout(self)
        

        x, y, w, h = 500, 200, 300, 400
        self.setGeometry(x, y, w, h)

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.tabs = QtWidgets.QTabWidget()
        self.main_layout.addWidget(self.tabs)
        
        self.tab_k150 = QtWidgets.QWidget()
        self.tabs.addTab(self.tab_k150, "K150")
        
        self.tab_about = AboutTab(self)
        self.tabs.addTab(self.tab_about, "About")

        
        self.combo = QtWidgets.QComboBox(self.tab_k150)
        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.combo.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.combo.completer().setFilterMode(QtCore.Qt.MatchContains)
        self.combo.completer().setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        
        #movemos combo (x,y)
        self.combo.move(480, 292)
        #seteamos el numero masximo de items que se pueden ver en el combo
        self.combo.setMaxVisibleItems(5)

        self.combo.highlighted.connect(self._cb_highlighted)
        self.combo.setFixedHeight(35)
        self.combo.setFixedWidth(100)

        items = ('','PIC12F508', 'PIC12F509', 'PIC12F635', 'PIC12F675', 'PIC12F683', 'PIC16F505', 'PIC16F506', 'PIC16F54', 'PIC16F57', 'PIC16F59', 'PIC16F627',
                 'PIC16LF627A', 'PIC16F627A', 'PIC16F628', 'PIC16LF628A', 'PIC16F628A', 'PIC16F630', 'PIC16F631', 'PIC16F636', 'PIC16F636-1', 'PIC16F639', 'PIC16F648A',
                 'PIC16F676', 'PIC16F677', 'PIC16F677-1', 'PIC16F684', 'PIC16F685', 'PIC16F685-1', 'PIC16F687', 'PIC16F687', 'PIC16F687-1', 'PIC16F688', 'PIC16F689',
                 'PIC16F689-1', 'PIC16F690', 'PIC16F690-1', 'PIC16F716', 'PIC16F72', 'PIC16F73', 'PIC16F74','PIC16F76', 'PIC16F77', 'PIC16F737', 'PIC16F747', 'PIC16F767',
                 'PIC16F777', 'PIC16F83', 'PIC16F84', 'PIC16F84A', 'PIC16F87', 'PIC16F88', 'PIC16F818', 'PIC16F819', 'PIC16F870', 'PIC16F871', 'PIC16F872', 'PIC16F873',
                 'PIC16F873A', 'PIC16LF873A', 'PIC16F874', 'PIC16F874A', 'PIC16F876', 'PIC16F876A', 'PIC16F877', 'PIC16F877A')
        self.combo.addItems(items)
        
        
# TODAS LAS TEXT EDIT
        #pantalla=QtWidgets.QTextEdit(self)
        #pantalla.setGeometry(QtCore.QRect(10, 0, 460, 266))
        #pantalla.setObjectName("pantalla")
        #pantalla.setText("Aqui van el archivo HEX \n falta mostrar el numero de linea esta aqui https://stackoverflow.com/questions/40386194/create-text-area-textedit-with-line-number-in-pyqt.")
        #pantalla.setStyleSheet("background-color: black;")        
        #self.pantalla.setStyleSheet("background-color: transparent;")

        self.pantalla=QCodeEditor(self.tab_k150)
        self.pantalla.setGeometry(QtCore.QRect(10, 0, 460, 266))
        self.pantalla.setObjectName("pantalla")
        #self.pantalla.setPlainText("Aqui van el archivo HEX, pero en binario y los numeros en la izquierda tambien son binario \n falta mostrar el numero de linea esta aqui https://stackoverflow.com/questions/40386194/create-text-area-textedit-with-line-number-in-pyqt.")
        self.pantalla.setStyleSheet("background-color: black; color: white;")
        
        # TODAS LAS LABELS
        #label 
        label1 = QtWidgets.QLabel(self.tab_k150)
        label1.setText("Chip Selector:")
        label1.move(480, 271)
        

        
        #label de la tarje
        #lboard = QtWidgets.QLabel(self)

        #label de Mensajes de ERORR o EXITO, mesajes filtraos de la terminal
        self.msg = QtWidgets.QLabel("<b>Dispositivo K150 no conectado</b>",self.tab_k150)
        self.msg.setStyleSheet("color: red; font-weight: bold;")
        self.msg.move(10, 450)        
        
      
        #label del puerto USB
        self.lusb = QtWidgets.QLabel("Port:                                                     ",self.tab_k150)
        self.lusb.move(100, 304)
        #self.lusb= QtGui.QLabel("f")
        #lusb.move(0, 271)

        #lusb.move(0,228)
        #lboard = QtWidgets.QLabel(self)
        #lboard.setText("Chip Selector:")
        #lboard.move(30, 10)  


        
        # Imagen posicion del PIC en el ZIF
        # Imagen posicion del PIC en el ZIF
        self.label = QtWidgets.QLabel(self.tab_k150)
        base_path = os.path.dirname(__file__) 
        # El archivo en assets/BITMAP es .bmp, no .png
        image_path = os.path.join(base_path, "assets", "BITMAP", "SOCKETS.bmp")
        pixmap = QtGui.QPixmap(image_path)
        
        self.label.setScaledContents(True)
        self.label.resize(114, 266)
        self.label.move(470, 0)

        if not pixmap.isNull():
            self.label.setPixmap(pixmap)
        else:
            self.label.setText("Imagen no encontrada")
            print(f"Error: No se pudo cargar {image_path}")

        # Conectar señal del combo ahora que todos los widgets existen
        self.combo.currentIndexChanged.connect(self._cb_currentIndexChanged)
        

        #self.bconect= QtWidgets.QPushButton("Conectar",self)
        #self.bconect.clicked.connect(self.port)
        #self.bconect.move(10, 10)        
            
        #Icono en la ventana
        image_path = os.path.join(base_path, "assets", "banner", "PikBurn.png")
        self.setWindowIcon(QtGui.QIcon(image_path))    
        
        #label 
        #label1 = QtWidgets.QLabel(self)
        #label1.setText("Chip Selector:")
        #label1.move(480, 271)
        


        # TODOS LOS BOTONES
        # boton conectar
        self.bconect= QtWidgets.QPushButton("Conectar",self.tab_k150)
        self.bconect.clicked.connect(self.port)
        self.bconect.move(10, 300)
        
        # boton Load
        self.bload= QtWidgets.QPushButton("Load",self.tab_k150)
        self.bload.clicked.connect(self.load_file_hex)
        self.bload.move(10, 340)        
        
        # boton Merge
        self.bmerge= QtWidgets.QPushButton("Merge",self.tab_k150)
        self.bmerge.clicked.connect(self.port)
        self.bmerge.move(110, 340)
        
        # boton Program
        self.bprogram= QtWidgets.QPushButton("Program",self.tab_k150)
        self.bprogram.clicked.connect(self.program)
        self.bprogram.move(210, 340)
        
        # boton Verify
        self.bverify= QtWidgets.QPushButton("Verify",self.tab_k150)
        self.bverify.clicked.connect(self.verify)
        self.bverify.move(310, 340)
        
        # boton Refresh
        self.brefresh= QtWidgets.QPushButton("Refresh",self.tab_k150)
        self.brefresh.clicked.connect(self.load_file_hex)
        self.brefresh.move(10, 390)        
        
        # boton Save
        self.bsave= QtWidgets.QPushButton("Save",self.tab_k150)
        self.bsave.clicked.connect(self.port)
        self.bsave.move(110, 390)
        
        # boton Read
        self.bread= QtWidgets.QPushButton("Read",self.tab_k150)
        self.bread.clicked.connect(self.read_pic)
        self.bread.move(210, 390)
        
        # boton Blank
        self.bblank= QtWidgets.QPushButton("Blank",self.tab_k150)
        self.bblank.clicked.connect(self.port)
        self.bblank.move(310, 390)
        
        
        # BARRA DE PROGRESO
        self.bar=QtWidgets.QProgressBar(self.tab_k150)
        self.bar.move(420, 446)
        self.bar.setFixedWidth(170)
        
        
        
    def text_change(self):       
        print("change ok")
    
    def text_click(event):
        print("clicked ok ")
        
# Funcion para conocer la posicion del combobox del selector de pic
    def _cb_currentIndexChanged(self, idx):
        # Evitar errores si se activa antes de que self.label exista
        if not hasattr(self, 'label'):
            return

        base_path = os.path.dirname(__file__) 
        print('current selected index:', idx)
        
        # Mapeo de índices a imágenes de pines (ajustado a .bmp en assets/BITMAP)
        image_name = "SOCKETS.bmp"
        
        if idx in (8, 16, 49, 50):
            image_name = "PIN18.bmp"
        elif idx == 6:
            image_name = "PIN1413.bmp"
        elif idx == 65:
            image_name = "PIN40.bmp"
            
        image_path = os.path.join(base_path, "assets", "BITMAP", image_name)
        pixmap = QtGui.QPixmap(image_path)
        
        if not pixmap.isNull():
            self.label.setPixmap(pixmap)
        else:
            print(f"Advertencia: No se pudo cargar {image_path}")
            default_path = os.path.join(base_path, "assets", "BITMAP", "SOCKETS.bmp")
            self.label.setPixmap(QtGui.QPixmap(default_path))
            
        # Corregimos el error de bconect si no existe aún (por si acaso)
        if hasattr(self, 'bconect'):
            self.bconect.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
            



    def _cb_highlighted(self, idx):
        print ('highlighted index:', idx)
        

    # Antiguo def port eliminado para evitar conflictos
            
            
# Funcion para cargar archivos HEX
#loader = QUiLoader()

#file = QFile(":/forms/myform.ui")

#file.open(QFile.ReadOnly)

#myWidget = loader.load(file, self)

#file.close()
            
            
                
    def load_file_hex(self):

        fname = QtWidgets.QFileDialog.getOpenFileName()
        ruta_load=fname[0]
        print(type(ruta_load))
        self.ruta_load_str=''.join(ruta_load)
        #leemos el archivo HEX
        leer_file=open(ruta_load,'r')
        texto=leer_file.read()
        leer_file.close()
        #Convertimos hex a binario
        #n_bits=8
        #scale=16
        #texto_bin=bin(int(texto, scale))[2:].zfill(num_of_bits)
        #decimal=int(texto,16)
        #texto_bin=bin(decimal)
        #setiamos en la pantalla
        self.pantalla.setPlainText(texto)  
        #self.pantalla.setText.toPlainText(fname)            
            
            
        
    #Funcion para conocer el puerto y el nombre de manufactura
    def port(self, checked=False):
        """
        Function for connect to the K150 device and find the port
        """
        puertos_disponibles = comports()
        
        if not puertos_disponibles:
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Dispositivo K150 No conectado")
            self.lusb.setText("Port: ")
            print("No se encontraron puertos COM.")
            return

        k150_port = puertos_disponibles[0]
        

        if k150_port.description:
            res_str = k150_port.description
            if "PHASED OUT" in res_str:
                self.msg.setStyleSheet("color: orange; font-weight: bold;")
                url = "https://github.com/polachp/pl2303-legacy-w11"
                texto_error = (
                    f"Error: Driver Prolific incompatible. "
                    f"<a href='{url}' style='color: #3498db;'>Descargar Driver Legacy aquí</a>"
                )
                
                self.msg.setOpenExternalLinks(True)
                self.msg.setText(texto_error)
                self.msg.adjustSize()
                return

        puerto_str = k150_port.device
        self.lusb.setText(f"Port: {puerto_str}")
        self.msg.setStyleSheet("color: #00AA00; font-weight: bold;") 
        self.msg.setText(f"Conexion Exitosa en el puerto: {k150_port.device}")
        self.msg.adjustSize()



    def program(self, checked=False):
        """
        Function for save the file HEX to the PIC
        """
        
        # 1. Validar puerto
        puerto_str = self.lusb.text().replace("Port: ", "").strip()
        if not puerto_str:
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Primero conecte el dispositivo.")
            self.msg.adjustSize()
            return

        # 2. Validar archivo HEX
        if not hasattr(self, 'ruta_load_str') or not self.ruta_load_str:
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Primero cargue un archivo HEX.")
            self.msg.adjustSize()
            return

        # 3. Validar PIC
        pic = self.combo.currentText()
        if not pic:
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Seleccione un chip de la lista.")
            self.msg.adjustSize()
            return
            
        if pic.startswith("PIC"):
            pic = pic[3:]

        self.bar.setRange(0, 100)
        self.bar.setValue(10)
        import os
        import subprocess

        # --- CONFIGURACIÓN DE RUTAS ---
        # Ruta de la carpeta donde están picpro.py y chipinfo.cid
        base_path = os.path.dirname(os.path.abspath(__file__))
        programmer_dir = os.path.join(base_path, "kitsrus_pic_programmer", "python 3")
        picpro_path = os.path.join(programmer_dir, "picpro.py")
        
        # Datos del formulario
        puerto_str = self.lusb.text().replace("Port: ", "").strip()
        pic = self.combo.currentText().replace("PIC", "") if self.combo.currentText() else ""
        hex_path = os.path.abspath(self.ruta_load_str) if hasattr(self, 'ruta_load_str') else ""

        if not puerto_str or not hex_path or not pic:
            self.msg.setText("Faltan datos (Puerto, PIC o Archivo)")
            self.msg.adjustSize()
            return

        # Comando con rutas entrecomilladas por si hay espacios
        command = [
            "python", f'"{picpro_path}"', 
            "-p", puerto_str, 
            f"--pic_type={pic}", 
            "-i", f'"{hex_path}"', 
            "--program"
        ]
        cmd_str = " ".join(command)

        try:
            self.bar.setValue(30)
            self.msg.setText("Grabando...")
            self.repaint()
            
            output = subprocess.check_output(
                cmd_str, 
                stderr=subprocess.STDOUT, 
                shell=True,
                cwd=programmer_dir  # <--- ESTO ES LO QUE HACE QUE ENCUENTRE EL .CID
            )
            
            self.bar.setValue(100)
            self.msg.setStyleSheet("color: green; font-weight: bold;")
            self.msg.setText("¡Grabación exitosa!")
            
        except subprocess.CalledProcessError as e:
            self.bar.setValue(0)
            error_output = e.output.decode("utf-8", errors="replace")
            print("Error:", error_output)
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            
            if "chipinfo.cid" in error_output.lower():
                self.msg.setText("Error: No se encuentra chipinfo.cid (revisa minúsculas)")
            else:
                self.msg.setText("Error en la grabación")
        
        self.msg.adjustSize()

    def verify(self, checked=False):
        """
        Function for verify the file HEX against the PIC
        """
        print("Entro al boton verify...")
        
        # Validar si hay puerto seleccionado
        puerto_str = self.lusb.text().replace("Port: ", "").strip()
        if not puerto_str:
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Primero conecte el dispositivo.")
            print("Error: No se ha conectado un dispositivo K150 (puerto vacio).")
            return

        # Validar si hay un archivo cargado
        if not hasattr(self, 'ruta_load_str') or not self.ruta_load_str:
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("El PIC no tiene archivo HEX cargado.")
            print("Error: No se ha cargado ningun archivo HEX.")
            return

        # Obtener el PIC seleccionado (removiendo 'PIC' del inicio si existe)
        pic = self.combo.currentText()
        if not pic:
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Seleccione un chip de la lista.")
            print("Error: No se ha seleccionado ningun chip de la lista desplegable.")
            return
            
        if pic.startswith("PIC"):
            pic = pic[3:]

        # Construir y ejecutar el comando
        import os
        base_path = os.path.dirname(__file__)
        picpro_path = os.path.join(base_path, "kitsrus_pic_programmer", "python 3", "picpro.py")
        
        command = [
            "python", f'"{picpro_path}"', 
            "-p", puerto_str, 
            f"--pic_type={pic}", 
            "-i", f'"{self.ruta_load_str}"', 
            "--verify"
        ]
        
        cmd_str = " ".join(command)
        self.msg.setStyleSheet("color: #00AA00; font-weight: bold;") 
        self.msg.setText(f"Verificando {pic} en {puerto_str}...")
        self.bar.setValue(10) # Un poco de feedback visual
        self.repaint() # Forzar actualizacion UI
        
        try:
            print("Ejecutando verificacion:", cmd_str)
            output = subprocess.check_output(cmd_str, stderr=subprocess.STDOUT, shell=True)
            self.bar.setValue(100)
            self.msg.setStyleSheet("color: #00AA00; font-weight: bold;") 
            self.msg.setText("Verificacion exitosa! El archivo coincide.")
            print("Resultado:", output.decode("utf-8", errors="replace"))
        except subprocess.CalledProcessError as e:
            self.bar.setValue(0)
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Error: El PIC no coincide con el archivo.")
            print("Error detallado:", e.output.decode("utf-8", errors="replace"))

    def read_pic(self):
        """
        Read the content of the PIC and show it on the screen.
        """
        print("Entro al boton Read...")
        puerto_str = self.lusb.text().replace("Port: ", "").strip()
        pic = self.combo.currentText().replace("PIC", "")

        if not puerto_str or not pic:
            self.msg.setText("Error: Conecte el programador y seleccione un PIC.")
            self.msg.adjustSize()
            return

        import os
        import subprocess

        base_path = os.path.dirname(os.path.abspath(__file__))
        programmer_dir = os.path.join(base_path, "kitsrus_pic_programmer", "python 3")
        picpro_path = os.path.join(programmer_dir, "picpro.py")
        output_hex = os.path.join(base_path, "leido.hex")

        command = [
            "python", f'"{picpro_path}"', 
            "-p", puerto_str, 
            f"--pic_type={pic}", 
            "-o", f'"{output_hex}"', 
            "--read"
        ]

        try:
            self.msg.setText("Leyendo PIC...")
            self.repaint()
            
            subprocess.check_output(" ".join(command), stderr=subprocess.STDOUT, shell=True, cwd=programmer_dir)
            
            # Si se leyó con éxito, cargamos el archivo en la pantalla
            if os.path.exists(output_hex):
                with open(output_hex, 'r') as f:
                    contenido = f.read()
                    self.pantalla.setPlainText(contenido)
                
                # Check if the PIC is blank
                es_blanco = True
                lineas = contenido.strip().split('\n')
                for linea in lineas:
                    if not linea.startswith(':') or len(linea) < 11:
                        continue
                    tipo = linea[7:9]
                    if tipo == '00': # Data record
                        longitud = int(linea[1:3], 16)
                        datos = linea[9:9+(longitud*2)]
                        # Si no es FF y no es 3F, entonces no está en blanco.
                        datos_leidos = datos.upper().replace('FF', '').replace('3F', '')
                        if datos_leidos != '':
                            es_blanco = False
                            break

                self.msg.setStyleSheet("color: #00AA00; font-weight: bold;")
                if es_blanco:
                    self.msg.setText("Lectura exitosa. ¡El PIC está EN BLANCO!")
                    self.msg.adjustSize()

                else:
                    self.msg.setText("Lectura exitosa. (El PIC contiene código)")
                    self.msg.adjustSize()

            
        except subprocess.CalledProcessError as e:
            print("Error:", e.output.decode("utf-8", errors="replace"))
            self.msg.setStyleSheet("color: red; font-weight: bold;")
            self.msg.setText("Error al leer el PIC.")


    def show_and_raise(self):
        self.show()
        self.raise_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)





    demo = Demo()
    # Tamaño de la ventana
    #demo.resize(ancho,alto)
    demo.resize(600,480)
    #NOmbre de la ventana
    demo.setWindowTitle("PikBurn")
    demo.show_and_raise()


    sys.exit(app.exec())
