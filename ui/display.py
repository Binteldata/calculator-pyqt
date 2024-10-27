# ui/display.py
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setFixedHeight(70)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setReadOnly(True)
        self.setText('0')
        self.setStyleSheet("""
            QLineEdit {
                background-color: #333333;
                color: white;
                border: none;
                font-size: 32px;
                padding: 10px;
            }
        """)
