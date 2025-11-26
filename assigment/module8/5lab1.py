def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1_str = input("Enter first number (or 'exit' to quit): ")
            if num1_str.lower() == 'exit':
                break
            num1 = float(num1_str)

            operator = input("Enter operator (+, -, *, /): ")
            if operator not in ['+', '-', '*', '/']:
                raise ValueError("Error: Invalid operator.")

            num2_str = input("Enter second number: ")
            num2 = float(num2_str)

            result = None
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)

            print(f"Result: {result}")

        except ValueError as e:
            print(e)
            print("Please enter valid numerical input for numbers.")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        print("-" * 30)

    print("Calculator exited. Goodbye!")

if __name__ == "__main__":
    calculator()