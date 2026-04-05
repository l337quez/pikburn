from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QHBoxLayout, QFrame)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os

class AboutTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        header_frame = QFrame()
        header_layout = QVBoxLayout(header_frame)
        
        self.logo_label = QLabel()
        self.logo_label.setFixedSize(120, 120)
        self.logo_label.setAlignment(Qt.AlignCenter)
        
        base_path = os.path.dirname(__file__) 
        image_path = os.path.join(base_path, "assets", "banner", "PikBurn.png")
        
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.logo_label.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.logo_label.setText("LOGO")
            self.logo_label.setStyleSheet("border: 1px solid #ccc; border-radius: 60px; background-color: #eee;")
        
        header_layout.addWidget(self.logo_label, alignment=Qt.AlignCenter)

        app_name = QLabel("Pikburn")
        app_name.setStyleSheet("font-size: 12px; font-weight: bold;")
        header_layout.addWidget(app_name, alignment=Qt.AlignCenter)

        main_layout.addWidget(header_frame)

        self.version_label = QLabel(
            "<b>Pikburn</b>, Tool for burning a PIC using the K150 burner"
        )
        self.version_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.version_label)

        # Labels Data Section
        labels_frame = QFrame()
        labels_frame.setStyleSheet("""
            QFrame {
                border: 1px solid rgba(128, 128, 128, 0.3);
                border-radius: 8px;
                background-color: rgba(128, 128, 128, 0.05);
            }
            QLabel {
                border: none;
                background-color: transparent;
            }
        """)
        labels_layout = QVBoxLayout(labels_frame)
        labels_layout.setSpacing(12)
        labels_layout.setContentsMargins(20, 20, 20, 20)

        labels_data = [
            ("version:", "v0.1.3 Beta"),
            ("license:", "GPL V3"),
            ("packaged:", "Ronal Forero"),
            ("tested:", "Ronal Forero"),
            ("Third-party code:", "Tony Nixon (kitsrus)"),
            ("development by:", "Ronal Forero")
        ]

        for title, value in labels_data:
            lbl = QLabel(f"<b>{title}</b> {value}")
            lbl.setAlignment(Qt.AlignCenter)
            labels_layout.addWidget(lbl)
        
        main_layout.addWidget(labels_frame)

        self.copyright_label = QLabel("Copyright © 2019 Ronal Forero. Licensed under GPL v3.")
        self.copyright_label.setStyleSheet("color: #95a5a6; font-size: 11px; margin-top: 20px;")
       
        self.copyright_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.copyright_label)

        main_layout.addStretch()

        self.setLayout(main_layout)
