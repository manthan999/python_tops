choice = 'y'
while choice != 'n':
  
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation: +, -, *, /")
    op = input("Enter operator: ")
    
    if op == '+':
        print("Result:", num1 + num2)
    elif op == '-':
        print("Result:", num1 - num2)
    elif op == '*':
        print("Result:", num1 * num2)
    elif op == '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero not allowed")
    else:
        print("Invalid operator")
    
    choice = input("Do you want to continue? (y/n): ")
