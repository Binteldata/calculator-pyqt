# ui/calculator_window.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from .display import Display
from .keypad import Keypad
from logic.calculator_logic import CalculatorLogic

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.calculator_logic = CalculatorLogic()
        
    def init_ui(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 500)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # Create display
        self.display = Display()
        layout.addWidget(self.display)
        
        # Create keypad
        self.keypad = Keypad(self.button_clicked)
        layout.addLayout(self.keypad)
    
    def button_clicked(self, text):
        result = self.calculator_logic.process_input(text)
        self.display.setText(result)