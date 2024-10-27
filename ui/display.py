# ui/display.py
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import Qt
from .styles import CalculatorStyles  # Import our new styles

class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setFixedHeight(70)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setReadOnly(True)
        self.setText('0')
        self.setStyleSheet(CalculatorStyles.get_display_style())  # Use our new styles