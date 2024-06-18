# Task 1: Create functions for each arithmetic operation.

def add(x, y):
    return x + y
def subtract(x, y): 
    return x - y    
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def exponent(x, y):
    return x ** y   
def modulus(x, y):
    return x % y
def floor_division(x, y):
    return x // y

# Task 2: Implement user input to receive numbers and an operation choice.
# operation = input("Enter the operation (+, -, *, /, **, %, //): ")
# x = float(input("Enter first number: "))
# y = float(input("Enter second number: "))

while True:
    operation = input("Enter the operation (+, -, *, /, **, %, //): ")
    if operation in ['+', '-', '*', '/', '**', '%', '//']:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError: # Task 3
            print("Invalid input. Please enter a number.") # Task 3
            continue
        if operation == '+':
            print(x, "+", y, "=", add(x, y))
        elif operation == '-':  
            print(x, "-", y, "=", subtract(x, y))   
        elif operation == '*':
            print(x, "*", y, "=", multiply(x, y))
        elif operation == '/':
            if y == 0:
                print("Division by zero is not allowed.") # Task 3
            print(x, "/", y, "=", divide(x, y))
        elif operation == '**':
            print(x, "**", y, "=", exponent(x, y))
        elif operation == '%':
            print(x, "%", y, "=", modulus(x, y))
        elif operation == '//':
            if y == 0:
                print("Division by zero is not allowed.") # Task 3
            print(x, "//", y, "=", floor_division(x, y))
        break
    else:
        print("Invalid input")

# Task 3: Ensure your program can handle division by zero and other potential errors.
# Added to the code above.

