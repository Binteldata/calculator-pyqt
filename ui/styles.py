# ui/styles.py

class CalculatorStyles:
    # Theme definitions
    DARK_THEME = {
        'background': '#1E1B18',    # Dark brown background
        'special': '#D8315B',       # Red for special buttons
        'operator': '#3E92CC',      # Light blue for operators
        'number': '#0A2463',        # Dark blue for numbers
        'text': '#EAE2B7',          # Cream color for text
        'border': '#FCBF49'         # Yellow for borders
    }
    
    LIGHT_THEME = {
        'background': '#FEFAE0',    # Light yellow background
        'special': '#BC6C25',       # Brown for special buttons
        'operator': '#606C38',      # Dark green for operators
        'number': '#283618',        # Dark green for numbers
        'text': '#FF0000',          # Red for text (display numbers)
        'border': '#283618'         # Dark green for borders
    }

    _current_theme = DARK_THEME  # Default theme

    @classmethod
    def toggle_theme(cls):
        cls._current_theme = cls.LIGHT_THEME if cls._current_theme == cls.DARK_THEME else cls.DARK_THEME
        return cls._current_theme

    @classmethod
    def get_current_theme(cls):
        return cls._current_theme

    @classmethod
    def get_main_widget_style(cls):
        return f"""
            QWidget {{
                background-color: {cls._current_theme['background']};
            }}
        """

    @classmethod
    def get_display_style(cls):
        return f"""
            QLineEdit {{
                background-color: {cls._current_theme['background']};
                color: {cls._current_theme['text']};
                border: 2px solid {cls._current_theme['border']};
                border-radius: 10px;
                font-size: 32px;
                padding: 10px;
                margin: 5px;
            }}
        """

    @classmethod
    def get_button_style(cls, style_type):
        styles = {
            'number': f"""
                QPushButton {{
                    background-color: {cls._current_theme['number']};
                    color: {cls._current_theme['text']};
                    font-size: 20px;
                    border: none;
                    border-radius: 25px;
                    padding: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                }}
                QPushButton:pressed {{
                    background-color: {cls._current_theme['number']}CC;
                    transform: translateY(2px);
                }}
            """,
            'operator': f"""
                QPushButton {{
                    background-color: {cls._current_theme['operator']};
                    color: {cls._current_theme['text']};
                    font-size: 20px;
                    border: none;
                    border-radius: 25px;
                    padding: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                }}
                QPushButton:pressed {{
                    background-color: {cls._current_theme['operator']}CC;
                    transform: translateY(2px);
                }}
            """,
            'special': f"""
                QPushButton {{
                    background-color: {cls._current_theme['special']};
                    color: {cls._current_theme['text']};
                    font-size: 20px;
                    border: none;
                    border-radius: 25px;
                    padding: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                }}
                QPushButton:pressed {{
                    background-color: {cls._current_theme['special']}CC;
                    transform: translateY(2px);
                }}
            """
        }
        return styles.get(style_type, styles['number'])

    @classmethod
    def get_theme_button_style(cls):
        return f"""
            QPushButton {{
                background-color: {cls._current_theme['special']};
                color: {cls._current_theme['text']};
                border: none;
                border-radius: 20px;
                font-size: 16px;
                padding: 5px;
            }}
            QPushButton:pressed {{
                background-color: {cls._current_theme['special']}CC;
            }}
        """