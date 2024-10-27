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