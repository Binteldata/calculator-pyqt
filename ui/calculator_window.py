# ui/calculator_window.py
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QHBoxLayout)
from .display import Display
from .keypad import Keypad
from logic.calculator_logic import CalculatorLogic
from .styles import CalculatorStyles

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.calculator_logic = CalculatorLogic()
        
    def init_ui(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 500)
        
        # Main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout()
        self.main_widget.setLayout(layout)
        
        # Apply background style
        self.main_widget.setStyleSheet(CalculatorStyles.get_main_widget_style())
        
        # Add theme toggle button
        theme_layout = QHBoxLayout()
        self.theme_button = QPushButton("🌙")  # Moon emoji for dark mode
        self.theme_button.setFixedSize(60, 60)
        self.theme_button.clicked.connect(self.toggle_theme)
        self.theme_button.setStyleSheet(CalculatorStyles.get_button_style('special'))
        theme_layout.addStretch()
        theme_layout.addWidget(self.theme_button)
        layout.addLayout(theme_layout)
        
        # Create display
        self.display = Display()
        layout.addWidget(self.display)
        
        # Create keypad
        self.keypad = Keypad(self.button_clicked)
        layout.addLayout(self.keypad)
    
    def button_clicked(self, text):
        result = self.calculator_logic.process_input(text)
        self.display.setText(result)
    
    def toggle_theme(self):
        # Toggle theme
        CalculatorStyles.toggle_theme()
        
        # Update UI elements
        self.main_widget.setStyleSheet(CalculatorStyles.get_main_widget_style())
        self.display.setStyleSheet(CalculatorStyles.get_display_style())
        self.theme_button.setText("☀️" if CalculatorStyles.get_current_theme() == CalculatorStyles.LIGHT_THEME else "🌙")
        self.theme_button.setStyleSheet(CalculatorStyles.get_button_style('special'))
        
        # Update all buttons in keypad
        for i in range(self.keypad.count()):
            widget = self.keypad.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                style_type = 'operator' if widget.text() in {'+', '-', '×', '÷', '='} else \
                           'special' if widget.text() in {'AC', '←', '%'} else 'number'
                widget.setStyleSheet(CalculatorStyles.get_button_style(style_type))