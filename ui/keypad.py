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