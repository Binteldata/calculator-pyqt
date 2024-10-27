# main.py
import sys
from PyQt6.QtWidgets import QApplication
from ui.calculator_window import CalculatorWindow

def main():
    app = QApplication(sys.argv)
    calculator = CalculatorWindow()
    calculator.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

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

# ui/keypad.py
from PyQt6.QtWidgets import QGridLayout, QPushButton
from functools import partial

class Keypad(QGridLayout):
    def __init__(self, button_callback):
        super().__init__()
        self.button_callback = button_callback
        self.init_buttons()
    
    def init_buttons(self):
        # Button data: text, position (row, column), span, style
        buttons = [
            ('AC', 0, 0, 1, 'special'),
            ('←', 0, 1, 1, 'special'),
            ('%', 0, 2, 1, 'special'),
            ('÷', 0, 3, 1, 'operator'),
            ('7', 1, 0, 1, 'number'),
            ('8', 1, 1, 1, 'number'),
            ('9', 1, 2, 1, 'number'),
            ('×', 1, 3, 1, 'operator'),
            ('4', 2, 0, 1, 'number'),
            ('5', 2, 1, 1, 'number'),
            ('6', 2, 2, 1, 'number'),
            ('-', 2, 3, 1, 'operator'),
            ('1', 3, 0, 1, 'number'),
            ('2', 3, 1, 1, 'number'),
            ('3', 3, 2, 1, 'number'),
            ('+', 3, 3, 1, 'operator'),
            ('0', 4, 0, 2, 'number'),
            ('.', 4, 2, 1, 'number'),
            ('=', 4, 3, 1, 'operator')
        ]
        
        for btn_text, row, col, span, style in buttons:
            button = QPushButton(btn_text)
            button.setStyleSheet(self.get_button_style(style))
            button.clicked.connect(partial(self.button_callback, btn_text))
            self.addWidget(button, row, col, 1, span)
    
    def get_button_style(self, style_type):
        styles = {
            'number': """
                QPushButton {
                    background-color: #505050;
                    color: white;
                    font-size: 20px;
                    border: none;
                    border-radius: 25px;
                    padding: 20px;
                }
                QPushButton:pressed {
                    background-color: #666666;
                }
            """,
            'operator': """
                QPushButton {
                    background-color: #FF9500;
                    color: white;
                    font-size: 20px;
                    border: none;
                    border-radius: 25px;
                    padding: 20px;
                }
                QPushButton:pressed {
                    background-color: #FFB143;
                }
            """,
            'special': """
                QPushButton {
                    background-color: #404040;
                    color: white;
                    font-size: 20px;
                    border: none;
                    border-radius: 25px;
                    padding: 20px;
                }
                QPushButton:pressed {
                    background-color: #666666;
                }
            """
        }
        return styles[style_type]

# logic/calculator_logic.py
class CalculatorLogic:
    def __init__(self):
        self.current_number = '0'
        self.stored_number = None
        self.operator = None
        self.new_number = True
    
    def process_input(self, text):
        if text.isdigit() or text == '.':
            return self._handle_number(text)
        elif text in {'+', '-', '×', '÷'}:
            return self._handle_operator(text)
        elif text == '=':
            return self._handle_equals()
        elif text == 'AC':
            return self._handle_clear()
        elif text == '←':
            return self._handle_backspace()
        elif text == '%':
            return self._handle_percentage()
        return self.current_number
    
    def _handle_number(self, text):
        if self.new_number:
            self.current_number = text
            self.new_number = False
        else:
            if text == '.' and '.' in self.current_number:
                return self.current_number
            self.current_number += text
        return self.current_number
    
    def _handle_operator(self, text):
        if self.stored_number is None:
            self.stored_number = float(self.current_number or '0')
        else:
            self._calculate()
        self.operator = text
        self.new_number = True
        return self.current_number
    
    def _handle_equals(self):
        self._calculate()
        self.operator = None
        self.new_number = True
        return self.current_number
    
    def _handle_clear(self):
        self.current_number = '0'
        self.stored_number = None
        self.operator = None
        self.new_number = True
        return '0'
    
    def _handle_backspace(self):
        if not self.new_number:
            self.current_number = self.current_number[:-1]
            if not self.current_number:
                self.current_number = '0'
        return self.current_number
    
    def _handle_percentage(self):
        if self.current_number:
            current = float(self.current_number)
            if self.stored_number is not None and self.operator:
                if self.operator in {'+', '-'}:
                    current = self.stored_number * (current / 100)
                else:
                    current = current / 100
            else:
                current = current / 100
            self.current_number = str(current)
        return self.current_number
    
    def _calculate(self):
        if self.stored_number is not None and self.current_number:
            try:
                current = float(self.current_number)
                if self.operator == '+':
                    result = self.stored_number + current
                elif self.operator == '-':
                    result = self.stored_number - current
                elif self.operator == '×':
                    result = self.stored_number * current
                elif self.operator == '÷':
                    if current == 0:
                        self._handle_clear()
                        return 'Error'
                    result = self.stored_number / current
                
                self.current_number = str(result)
                self.stored_number = result
            except Exception:
                self._handle_clear()
                return 'Error'
        return self.current_number

# Directory structure:
'''
calculator/
│
├── main.py
│
├── ui/
│   ├── __init__.py
│   ├── calculator_window.py
│   ├── display.py
│   └── keypad.py
│
└── logic/
    ├── __init__.py
    └── calculator_logic.py
'''