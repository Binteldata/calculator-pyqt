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
