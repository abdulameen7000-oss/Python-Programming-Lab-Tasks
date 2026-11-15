#Write a python program to print the multiplication table of a number

#1. using for loop
num = int(input("enter a number:"))
for multiplier in range (1, 11):
    product = num * multiplier
    print(f"{num} x {multiplier} = {product}")



#2. using while loop
number = int(input("Enter a number: "))

multiplier = 1
while multiplier <= 10:
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
    multiplier = multiplier + 1