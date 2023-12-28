# calculator.py

def add(x, y):
    result = x + y
    if result > 10:
        print("Result is greater than 10!")
    return result

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def is_positive(x):
    return x > 0

def power(x, exponent):
    return x ** exponent
