def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

# Function to display available operations
def display_operations():
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

# Take user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display available operations
display_operations()

# Take user input for operation choice
operation = input("Enter the operation number (1-4): ")

# Perform calculation based on operation choice
if operation == '1':
    result = add(num1, num2)
    print(f"Result: {num1} + {num2} = {result}")
elif operation == '2':
    result = subtract(num1, num2)
    print(f"Result: {num1} - {num2} = {result}")
elif operation == '3':
    result = multiply(num1, num2)
    print(f"Result: {num1} * {num2} = {result}")
elif operation == '4':
    result = divide(num1, num2)
    print(f"Result: {num1} / {num2} = {result}")
else:
    print("Invalid operation number. Please enter a number between 1 and 4.")
