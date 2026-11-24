#Implement a Python program that defines a function to convert temperature from Celsius to Fahrenheit (Celsius as parameter) and returns the result

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c = float(input("Enter temperature in Celsius: "))

result = celsius_to_fahrenheit(c)

print("Temperature in Fahrenheit:", result)