#Implement a Python program that defines a function divide(a, b) returning a / b; call it with keyword arguments divide(b=10, a=20) and with positional arguments divide(10, 20), and print both results

def divide(a, b):
    return a / b

# Keyword arguments
result1 = divide(b=10, a=20)
print("Keyword Arguments:", result1)

# Positional arguments
result2 = divide(10, 20)
print("Positional Arguments:", result2)