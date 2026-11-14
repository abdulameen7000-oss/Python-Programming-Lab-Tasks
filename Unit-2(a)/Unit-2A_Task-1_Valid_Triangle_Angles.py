# Write a python program to check whether a triangle is valid given its three angles

# Input three angles
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

# Check whether the triangle is valid
if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")