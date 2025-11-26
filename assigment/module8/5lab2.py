try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2
    print(f"The result of {num1} / {num2} is {result}")

    my_list = [1, 2, 3]
    index = int(input("Enter an index to access in the list [0-2]: "))
    print(f"Element at index {index} is {my_list[index]}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
 
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

except IndexError:
    print("Error: List index out of range.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Program execution completed.")
