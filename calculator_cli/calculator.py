"""
File: calculator.py
Description: A Command-Line Calculator that supports basic arithmetic operations
and includes error handling, clean structure, and user-friendly interaction.
"""

import sys

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division result, handling division by zero."""
    if b == 0:
        return "Error: Division by zero."
    return a / b

def get_numbers():
    """Get two valid float numbers from the user."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

def display_menu():
    """Display the available operations."""
    print("\n========== PYTHON CLI CALCULATOR ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("===========================================")

def main():
    """Main program logic."""
    while True:
        display_menu()
        choice = input("Enter your choice (1–5): ").strip()

        if choice == '5':
            print("Exiting the Calculator.")
            sys.exit(0)

        operations = {
            '1': ('+', add),
            '2': ('-', subtract),
            '3': ('*', multiply),
            '4': ('/', divide)
        }

        if choice not in operations:
            print("Invalid choice. Please select a valid option (1-5).")
            continue

        num1, num2 = get_numbers()
        symbol, operation = operations[choice]
        result = operation(num1, num2)

        print(f"\nResult: {num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting safely...")
        sys.exit(0)
