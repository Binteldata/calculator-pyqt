# PyQt6 Calculator

This project is a simple, functional GUI calculator built using Python and PyQt6. It supports basic arithmetic operations like addition, subtraction, multiplication, and division, with a modern and clean design.

## Features

- **Basic Operations**: Supports addition (`+`), subtraction (`-`), multiplication (`×`), and division (`÷`).
- **Clear and Backspace**: Includes functionality to clear (`AC`) or backspace (`←`).
- **Percentage**: Calculate percentage (`%`).
- **Responsive Display**: Shows input and results in a styled display widget.
- **Keypad**: Designed with a visually appealing layout, with distinct styles for number buttons, operator buttons, and special functions.

## Structure

The project is structured into two main parts:

- `ui/`: Contains the user interface components such as the main calculator window, display, and keypad.
- `logic/`: Contains the core logic for handling arithmetic operations.

## Requirements
To run the project, make sure you have the following installed:

- Python 3.x
- Pyqt6

## Install Dependencies

You can install the necessary dependencies using the following command:

- pip install PyQt6

## Running the Application 
After installing the required packages, run the application with:
- python main.py

## How It Works
1. **Display**: Shows the current input or result. It updates every time the user presses a button.
2. **Keypad**: Contains numbers (0-9), operators (+, -, ×, ÷), and special keys (AC, ←, =, %).
3. **Logic**: Each button click is processed by the calculator logic to compute results or modify the input.

## Contributing
Feel free to fork this repository, experiment with the code, and contribute.
This is a learning project, and collaboration is welcome! Let’s grow our Python and GUI development skills together.

## Directory Layout

```bash
calculator/
│
├── main.py              # Entry point of the application
│
├── ui/
│   ├── calculator_window.py   # Main window of the calculator
│   ├── display.py             # The display widget showing input/output
│   └── keypad.py              # The keypad with number, operator, and special buttons
│
└── logic/
    └── calculator_logic.py    # Handles calculation logic and button input processing

